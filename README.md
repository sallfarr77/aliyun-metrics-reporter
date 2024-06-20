# Aliyun Metrics Reporter

Aliyun Metrics Reporter is a tool for collecting and analyzing metrics from Aliyun ECS instances and saving them into a CSV file.

## Features

- Fetches CPU Utilization, Memory Utilization, Disk Read BPS, and Disk Write BPS metrics from Aliyun ECS instances.
- Saves metric data into a CSV file.
- Uses environment variables to store Aliyun credentials.

## Requirements

- Python 3.x
- Aliyun account with access to ECS API.
- `.env` file to store Aliyun credentials.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/sallfarr77/aliyun-metrics-reporter.git
    cd aliyun-metrics-reporter
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project directory and add your Aliyun credentials

5. Prepare a `instance_ids.txt` file containing ECS instance IDs, one ID per line.

## Usage

Run the main script to fetch metrics and save them into a CSV file:

```bash
python3 main.py
