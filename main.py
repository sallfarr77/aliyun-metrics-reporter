import datetime
import json
import csv
from aliyunsdkcore.client import AcsClient
from aliyunsdkcms.request.v20190101.DescribeMetricListRequest import DescribeMetricListRequest
from dotenv import load_dotenv
import os

# Memuat variabel lingkungan dari file .env
load_dotenv()

# Mendapatkan kredensial dari variabel lingkungan
ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
ACCESS_KEY_SECRET = os.getenv('ACCESS_KEY_SECRET')
REGION_ID = os.getenv('REGION_ID')

# Inisialisasi client
client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION_ID)

# Fungsi untuk mengambil metrik
def get_metric_data(metric_name, namespace, dimensions, period='86400', start_time=None, end_time=None):
    request = DescribeMetricListRequest()
    request.set_MetricName(metric_name)
    request.set_Namespace(namespace)
    request.set_Period(period)
    request.set_StartTime(start_time)
    request.set_EndTime(end_time)
    request.set_Dimensions(dimensions)

    response = client.do_action_with_exception(request)
    response = json.loads(response)

    return json.loads(response['Datapoints'])

# Fungsi untuk mendapatkan nilai minimum dan maksimum
def get_min_max(data, key):
    values = [float(dp[key]) for dp in data if key in dp]
    return min(values), max(values)

# Fungsi untuk mengubah nilai dari byte ke kilobyte
def bytes_to_kilobytes(bytes):
    return bytes / 1024

# Fungsi untuk menulis data ke dalam file CSV
def write_to_csv(filename, instance_ids, rows):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Menulis header
        writer.writerow(['Instance ID', 'Lowest CPU Utilization', 'Highest CPU Utilization', 'Lowest Memory Utilization', 'Highest Memory Utilization',
                         'Lowest Disk Read BPS', 'Highest Disk Read BPS', 'Lowest Disk Write BPS', 'Highest Disk Write BPS'])
        # Menulis data
        for instance_id, row in zip(instance_ids, rows):
            writer.writerow([instance_id] + row)

# Set parameter waktu
end_time = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
start_time = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")

# Baca instance IDs dari file
with open('instance_ids.txt', 'r') as f:
    instance_ids = f.readlines()
instance_ids = [x.strip() for x in instance_ids]

# Inisialisasi list untuk menyimpan semua data
all_data = []

# Loop untuk setiap instance ID
for instance_id in instance_ids:
    # Set dimensions
    dimensions = f'[{{"instanceId": "{instance_id}"}}]'

    # Ambil data metrik untuk setiap instance
    cpu_data = get_metric_data("CPUUtilization", "acs_ecs_dashboard", dimensions, start_time=start_time, end_time=end_time)
    memory_data = get_metric_data("memory_usedutilization", "acs_ecs_dashboard", dimensions, start_time=start_time, end_time=end_time)
    disk_read_data = get_metric_data("DiskReadBPS", "acs_ecs_dashboard", dimensions, start_time=start_time, end_time=end_time)
    disk_write_data = get_metric_data("DiskWriteBPS", "acs_ecs_dashboard", dimensions, start_time=start_time, end_time=end_time)

    # CPU Utilization
    min_cpu, max_cpu = get_min_max(cpu_data, 'Maximum')

    # Memory Utilization
    min_memory, max_memory = get_min_max(memory_data, 'Maximum')

    # Disk Read BPS
    min_disk_read, max_disk_read = get_min_max(disk_read_data, 'Maximum')

    # Disk Write BPS
    min_disk_write, max_disk_write = get_min_max(disk_write_data, 'Maximum')

    # Menambahkan data ke dalam list all_data
    all_data.append([
        f'{min_cpu:.2f}%', f'{max_cpu:.2f}%',
        f'{min_memory:.2f}%', f'{max_memory:.2f}%',
        f'{bytes_to_kilobytes(min_disk_read):.2f} KB', f'{bytes_to_kilobytes(max_disk_read):.2f} KB',
        f'{bytes_to_kilobytes(min_disk_write):.2f} KB', f'{bytes_to_kilobytes(max_disk_write):.2f} KB'
    ])

# Menulis data ke dalam file CSV
write_to_csv('metrics.csv', instance_ids, all_data)

print("Execution completed successfully!")
