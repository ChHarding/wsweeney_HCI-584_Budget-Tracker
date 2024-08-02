# Expense Tracker Project

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Limitations](#limitations)
- [Developer Documentation](#developer-documentation)

## Introduction
Welcome to the Expense Tracker! This project is designed to help you, esteemed user, manage and track your expenses efficiently. You can add, view, summarize, and delete expenses, and view summaries by category.

## Installation
Assuming you have cloned or downloaded the repository into a folder, please follow the steps below to set up and use the Expense Tracker.

## Setup
1. **Python Environment**: Please ensure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).
2. **Dependencies**: Kindly install the required dependencies. Navigate to the project folder and run:
   ```bash
   pip install -r requirements.txt
## Usage
To run the Expense Tracker, please execute the main script:

python src/main.py
### Main Menu
Upon running the script, you will see the following options:

1. Add an expense to a new file
2. Summarize a file by category
3. Add an expense to an existing file
4. View the content of a file
5. Delete a file
6. Summarize all files by category
7. Exit

Please enter the corresponding number to select a task.

### Adding an Expense
- Select option `1` to add an expense to a new file.
- Enter the date in the format mm-dd-yyyy.
- Provide the details for the expense, including name, amount, and category.
- Continue adding expenses or exit.
### Summarizing a File
- Select option `2` to summarize a file by category.
- Choose the file date from the list.
- View the summarized expenses by category and total amount.
### Adding an Expense to an Existing File
- Select option `3`.
- Choose the file date from the list.
- Add expenses as described in "Adding an Expense".
### Viewing File Content
- Select option `4`.
- Choose the file date from the list.
- View all expenses in the selected file.
### Deleting a File
- Select option `5`.
- Choose the file date from the list.
- Confirm deletion.
### Summarizing All Files
- Select option `6`.
- View a summary of all expenses by category and total amount.

## Troubleshooting
Here are some common issues you might encounter:

- Invalid Task: If you enter an invalid task number, you will see an "Invalid task. Please try again!" message.
- File Not Found: Ensure the file name is correct when accessing existing files.
- Invalid Date Format: Enter the date in mm-dd-yyyy format.

## Limitations
Please note the following limitations:

- The budget is currently fixed at $2000. This can be made dynamic if needed.
- The application only supports .pkl file format for storing expenses.

## Developer Documentation
For more technical details and development guidelines, please refer to the Developer Documentation.

## Notes
- Ensure all expense files are in the same directory as the script.
- Future versions may include enhancements like dynamic budgets and additional file formats.
