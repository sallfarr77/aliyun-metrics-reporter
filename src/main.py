from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv
from ecs_client import get_instance_name
from cms_client import get_metric_data
from metrics import get_min_max_avg
from utils import bytes_to_kilobytes, write_to_csv

# Load environment variables from .env file
load_dotenv()

# Read configuration from environment variables
instance_ids_file = os.getenv('INSTANCE_IDS_FILE', 'instance_ids.txt')
output_csv = os.getenv('OUTPUT_CSV', 'metrics.csv')
days_delta = int(os.getenv('DAYS_DELTA', 30))

# Set time parameters
end_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
start_time = (datetime.now(timezone.utc) - timedelta(days=days_delta)).strftime("%Y-%m-%dT%H:%M:%SZ")

# Read instance IDs from file
with open(instance_ids_file, 'r') as f:
    instance_ids = f.readlines()
instance_ids = [x.strip() for x in instance_ids]

# Initialize list to store all data
all_data = []

# Loop for each instance ID
for instance_id in instance_ids:
    # Get instance name
    instance_name = get_instance_name(instance_id)
    
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
        instance_name,
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
write_to_csv(output_csv, all_data)

print(f"Execution completed successfully! See {output_csv}")
