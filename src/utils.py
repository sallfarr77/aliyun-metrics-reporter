import csv

def bytes_to_kilobytes(bytes):
    return bytes / 1024

def write_to_csv(filename, rows):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Writing header
        writer.writerow([
            'Instance ID', 'Instance Name', 'Lowest CPU Utilization', 'Highest CPU Utilization', 'Average CPU Utilization',
            'Lowest Memory Utilization', 'Highest Memory Utilization', 'Average Memory Utilization',
            'Lowest Disk Read BPS', 'Highest Disk Read BPS', 'Average Disk Read BPS',
            'Lowest Disk Write BPS', 'Highest Disk Write BPS', 'Average Disk Write BPS'
        ])
        # Writing data
        writer.writerows(rows)
