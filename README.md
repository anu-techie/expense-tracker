# Expense Tracker CLI

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?logo=python)](https://www.python.org/)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey)](https://creativecommons.org/licenses/by-nc/4.0/)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Stars](https://img.shields.io/github/stars/anu-techie/expense-tracker?style=social)

>A simple yet powerful command-line tool to **track, manage, and analyze personal expenses** using Python.

---

## Requirements

- Python 3.x  
- No external dependencies — uses only built-in Python modules (`argparse`, `json`, `csv`, `datetime`, `os`)

---

## Features

- Add new expenses with description, amount, date, and category  
- Update existing expense entries  
- Delete expenses by ID  
- View all expenses or filter by category  
- Get a summary of total expenses  
- View monthly expense summary (current year)  
- Set and track monthly budgets — get a warning if exceeded  
- Export all expense records to CSV  
- Input validations for negative amounts, invalid dates, and missing fields

---

## What You'll Learn

- How to structure a command-line application with `argparse`  
- How to store and retrieve data using JSON files  
- How to build reusable functions and handle edge cases  
- How to read/write CSV files with the `csv` module  
- How to build real-world projects using only core Python

---

## Installation

1. **Download or Clone the Repository**

   - Download ZIP via **Code > Download ZIP**  
   - Or clone using Git:
     ```bash
     git clone https://github.com/anu-techie/expense_tracker_cli.git
     ```

2. **Navigate to Project Directory**
   ```bash
   cd expense-tracker_cli
   ```

3. **Ensure you have Python 3 & installed**

    ```bash
   python --version
   ```
   If Python is not installed, download it from python.org.

4. **Run the Task Tracker CLI**
    ```bash
    python expense_tracker.py --help
    ```
    To see available commands

---

## Data Files

- `expense_file.json` – Stores all expense records

- `budget_file.json` – Stores budget information per month

- `expenses_export.csv` – Exported file for reports/sharing

---

## Project URL

For detailed project guidelines and ideas, visit:
[https://roadmap.sh/projects/expense-tracker](https://roadmap.sh/projects/expense-tracker)

---

## Acknowledgments

This project was inspired by and developed following the excellent guidance from [roadmap.sh](https://roadmap.sh). Special thanks to their clear tutorials and project ideas.

---

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0).  
You can view the full license [here](https://creativecommons.org/licenses/by-nc/4.0/).

---

🙋‍♀️ Author : Anusuyadevi |   Learning Python building cool projects ❤️