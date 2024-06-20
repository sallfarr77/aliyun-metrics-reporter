import datetime
import json
import csv
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

# Function to get minimum and maximum values
def get_min_max(data, key):
    values = [float(dp[key]) for dp in data if key in dp]
    return min(values), max(values)

# Function to calculate average value
def get_average(data, key):
    values = [float(dp[key]) for dp in data if key in dp]
    return sum(values) / len(values) if values else 0

# Function to convert a value from bytes to kilobytes
def bytes_to_kilobytes(bytes):
    return bytes / 1024

# Function to write data into a CSV file with average values
def write_to_csv(filename, instance_ids, rows, averages):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(['Instance ID', 'Average CPU Utilization', 'Lowest CPU Utilization', 'Highest CPU Utilization', 
                         'Average Memory Utilization', 'Lowest Memory Utilization', 'Highest Memory Utilization',
                         'Average Disk Read BPS', 'Lowest Disk Read BPS', 'Highest Disk Read BPS',
                         'Average Disk Write BPS', 'Lowest Disk Write BPS', 'Highest Disk Write BPS'])
        # Write data
        for instance_id, row, average in zip(instance_ids, rows, averages):
            writer.writerow([instance_id] + average + row)

# Set time parameters
end_time = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
start_time = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")

# Read instance IDs from file
with open('instance_ids.txt', 'r') as f:
    instance_ids = f.readlines()
instance_ids = [x.strip() for x in instance_ids]

# Initialize lists to store average data
average_data = []

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
    min_cpu, max_cpu = get_min_max(cpu_data, 'Maximum')
    avg_cpu = get_average(cpu_data, 'Average')

    # Memory Utilization
    min_memory, max_memory = get_min_max(memory_data, 'Maximum')
    avg_memory = get_average(memory_data, 'Average')

    # Disk Read BPS
    min_disk_read, max_disk_read = get_min_max(disk_read_data, 'Maximum')
    avg_disk_read = get_average(disk_read_data, 'Average')

    # Disk Write BPS
    min_disk_write, max_disk_write = get_min_max(disk_write_data, 'Maximum')
    avg_disk_write = get_average(disk_write_data, 'Average')

    # Add data to the average_data list
    average_data.append([
        f'{avg_cpu:.2f}%', f'{min_cpu:.2f}%', f'{max_cpu:.2f}%',
        f'{avg_memory:.2f}%', f'{min_memory:.2f}%', f'{max_memory:.2f}%',
        f'{bytes_to_kilobytes(avg_disk_read):.2f} KB', f'{bytes_to_kilobytes(min_disk_read):.2f} KB', f'{bytes_to_kilobytes(max_disk_read):.2f} KB',
        f'{bytes_to_kilobytes(avg_disk_write):.2f} KB', f'{bytes_to_kilobytes(min_disk_write):.2f} KB', f'{bytes_to_kilobytes(max_disk_write):.2f} KB'
    ])

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
    min_cpu, max_cpu = get_min_max(cpu_data, 'Maximum')

    # Memory Utilization
    min_memory, max_memory = get_min_max(memory_data, 'Maximum')

    # Disk Read BPS
    min_disk_read, max_disk_read = get_min_max(disk_read_data, 'Maximum')

    # Disk Write BPS
    min_disk_write, max_disk_write = get_min_max(disk_write_data, 'Maximum')

    # Add data to the all_data list
    all_data.append([
        f'{min_cpu:.2f}%', f'{max_cpu:.2f}%',
        f'{min_memory:.2f}%', f'{max_memory:.2f}%',
        f'{bytes_to_kilobytes(min_disk_read):.2f} KB', f'{bytes_to_kilobytes(max_disk_read):.2f} KB',
        f'{bytes_to_kilobytes(min_disk_write):.2f} KB', f'{bytes_to_kilobytes(max_disk_write):.2f} KB'
    ])

# Write data into a CSV file
write_to_csv('metrics.csv', instance_ids, all_data, average_data)

print("Execution completed successfully!, see metrics.csv")
