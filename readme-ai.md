<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">ALIYUN-METRICS-REPORTER</h1>
</p>
<p align="center">
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/sallfarr77/aliyun-metrics-reporter?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/sallfarr77/aliyun-metrics-reporter?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/sallfarr77/aliyun-metrics-reporter?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/sallfarr77/aliyun-metrics-reporter?style=default&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

<code>Aliyun Metrics Reporter is a tool for reporting and analyzing ECS and CMS metrics from Aliyun. This tool collects metric data from various ECS instances and stores it in a CSV file for further analysis.</code>

---

##  Features

- Retrieves metrics such as CPU utilization, memory usage, and disk I/O from Aliyun ECS and CMS.
- Generates a CSV report summarizing metrics for specified instances over a specified period.
- Supports dynamic configuration via environment variables loaded from `.env`.

---

##  Repository Structure

```sh
└── aliyun-metrics-reporter/
    ├── LICENSE
    ├── README.md
    ├── instance_ids.txt
    ├── metrics.csv
    ├── requirements.txt
    ├── src
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── cms_client.py
    │   ├── ecs_client.py
    │   ├── main.py
    │   ├── metrics.py
    │   └── utils.py
    └── test

```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                                   | Summary                         |
| ---                                                                                                    | ---                             |
| [requirements.txt](https://github.com/sallfarr77/aliyun-metrics-reporter/blob/master/requirements.txt) | <code>► INSERT-TEXT-HERE</code> |
| [instance_ids.txt](https://github.com/sallfarr77/aliyun-metrics-reporter/blob/master/instance_ids.txt) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>src</summary>

| File                                                                                                 | Summary                         |
| ---                                                                                                  | ---                             |
| [metrics.py](https://github.com/sallfarr77/aliyun-metrics-reporter/blob/master/src/metrics.py)       | <code>► INSERT-TEXT-HERE</code> |
| [cms_client.py](https://github.com/sallfarr77/aliyun-metrics-reporter/blob/master/src/cms_client.py) | <code>► INSERT-TEXT-HERE</code> |
| [utils.py](https://github.com/sallfarr77/aliyun-metrics-reporter/blob/master/src/utils.py)           | <code>► INSERT-TEXT-HERE</code> |
| [main.py](https://github.com/sallfarr77/aliyun-metrics-reporter/blob/master/src/main.py)             | <code>► INSERT-TEXT-HERE</code> |
| [ecs_client.py](https://github.com/sallfarr77/aliyun-metrics-reporter/blob/master/src/ecs_client.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

---

##  Getting Started

**System Requirements:**

* **Python**: `version 3.y.z`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the aliyun-metrics-reporter repository:
>
> ```console
> $ git clone https://github.com/sallfarr77/aliyun-metrics-reporter
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd aliyun-metrics-reporter
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run aliyun-metrics-reporter using the command below:
> ```console
> $ python src/main.py
> ```

###  Tests

> Run the test suite using the command below:
> ```console
> $ pytest
> ```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/sallfarr77/aliyun-metrics-reporter/issues)**: Submit bugs found or log feature requests for the `aliyun-metrics-reporter` project.
- **[Submit Pull Requests](https://github.com/sallfarr77/aliyun-metrics-reporter/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/sallfarr77/aliyun-metrics-reporter/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/sallfarr77/aliyun-metrics-reporter
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/sallfarr77/aliyun-metrics-reporter/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=sallfarr77/aliyun-metrics-reporter">
   </a>
</p>
</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-overview)

---
