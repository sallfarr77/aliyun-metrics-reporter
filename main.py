import datetime
import json
import csv
import statistics
from aliyunsdkcore.client import AcsClient
from aliyunsdkcms.request.v20190101.DescribeMetricListRequest import DescribeMetricListRequest
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
ACCESS_KEY_SECRET = os.getenv('ACCESS_KEY_SECRET')
REGION_ID = os.getenv('REGION_ID')

# Client initialization
client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION_ID)

# Function to retrieve metrics
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

# Function to get minimum, maximum, and average values
def get_min_max_avg(data, key):
    values = [float(dp[key]) for dp in data if key in dp]
    if values:
        return min(values), max(values), statistics.mean(values)
    else:
        return None, None, None

# Function to convert a value from bytes to kilobytes
def bytes_to_kilobytes(bytes):
    return bytes / 1024

# Function to write data into a CSV file
def write_to_csv(filename, instance_ids, rows):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Writing header
        writer.writerow(['Instance ID', 'Lowest CPU Utilization', 'Highest CPU Utilization', 'Average CPU Utilization',
                         'Lowest Memory Utilization', 'Highest Memory Utilization', 'Average Memory Utilization',
                         'Lowest Disk Read BPS', 'Highest Disk Read BPS', 'Average Disk Read BPS',
                         'Lowest Disk Write BPS', 'Highest Disk Write BPS', 'Average Disk Write BPS'])
        # Writing data
        writer.writerows(rows)

# Set time parameters
end_time = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
start_time = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")

# Read instance IDs from file
with open('instance_ids.txt', 'r') as f:
    instance_ids = f.readlines()
instance_ids = [x.strip() for x in instance_ids]

# Initialize list to store all data
all_data = []

# Loop for each instance ID
for instance_id in instance_ids:
    # Set dimensions
    dimensions = f'[{{"instanceId": "{instance_id}"}}]'

    # Retrieve metric data for each instance
    cpu_data = get_metric_data("CPUUtilization", "acs_ecs_dashboard", dimensions, start_time=start_time, end_time=end_time)
    memory_data = get_metric_data("memory_usedutilization", "acs_ecs_dashboard", dimensions, start_time=start_time, end_time=end_time)
    disk_read_data = get_metric_data("DiskReadBPS", "acs_ecs_dashboard", dimensions, start_time=start_time, end_time=end_time)
    disk_write_data = get_metric_data("DiskWriteBPS", "acs_ecs_dashboard", dimensions, start_time=start_time, end_time=end_time)

    # CPU Utilization
    min_cpu, max_cpu, avg_cpu = get_min_max_avg(cpu_data, 'Maximum')

    # Memory Utilization
    min_memory, max_memory, avg_memory = get_min_max_avg(memory_data, 'Maximum')

    # Disk Read BPS
    min_disk_read, max_disk_read, avg_disk_read = get_min_max_avg(disk_read_data, 'Maximum')

    # Disk Write BPS
    min_disk_write, max_disk_write, avg_disk_write = get_min_max_avg(disk_write_data, 'Maximum')

    # Append row to all_data
    all_data.append([
        instance_id,
        f'{min_cpu:.2f}%' if min_cpu is not None else 'null',
        f'{max_cpu:.2f}%' if max_cpu is not None else 'null',
        f'{avg_cpu:.2f}%' if avg_cpu is not None else 'null',
        f'{min_memory:.2f}%' if min_memory is not None else 'null',
        f'{max_memory:.2f}%' if max_memory is not None else 'null',
        f'{avg_memory:.2f}%' if avg_memory is not None else 'null',
        f'{bytes_to_kilobytes(min_disk_read):.2f} KB' if min_disk_read is not None else 'null',
        f'{bytes_to_kilobytes(max_disk_read):.2f} KB' if max_disk_read is not None else 'null',
        f'{bytes_to_kilobytes(avg_disk_read):.2f} KB' if avg_disk_read is not None else 'null',
        f'{bytes_to_kilobytes(min_disk_write):.2f} KB' if min_disk_write is not None else 'null',
        f'{bytes_to_kilobytes(max_disk_write):.2f} KB' if max_disk_write is not None else 'null',
        f'{bytes_to_kilobytes(avg_disk_write):.2f} KB' if avg_disk_write is not None else 'null'
    ])

# Write data into a CSV file
write_to_csv('metrics.csv', instance_ids, all_data)

print("Execution completed successfully! See metrics.csv")
