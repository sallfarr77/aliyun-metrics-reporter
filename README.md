# Aliyun Metrics Reporter

Aliyun Metrics Reporter is a tool for reporting and analyzing ECS and CMS metrics from Aliyun. This tool collects metric data from various ECS instances and stores it in a CSV file for further analysis.

## Features

- Retrieves ECS instance names based on instance IDs.
- Fetches CPU, memory, disk read, and disk write metrics from Aliyun CMS.
- Computes minimum, maximum, and average values of the fetched metrics.
- Stores metric data into a CSV file for easy analysis.

## Requirements

- Python 3.6 or newer
- Aliyun account with access to ECS and CMS services
- Environment variables configured in a `.env` file (see `.env.example` for required variables)

## Installation

1. Clone the repository:

git clone https://github.com/yourusername/aliyun-metrics-reporter.git
cd aliyun-metrics-reporter


2. Install dependencies:

pip install -r requirements.txt

3. Set up your `.env` file with your Aliyun credentials:

mv .env.example .env

## Usage

Run the main script to fetch and store metrics:

python3 src/main.py


This will retrieve metrics for the ECS instances listed in `instance_ids.txt` and store the results in `metrics.csv`.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug fixes, please open an issue or a pull request on [GitHub](https://github.com/yourusername/aliyun-metrics-reporter).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
