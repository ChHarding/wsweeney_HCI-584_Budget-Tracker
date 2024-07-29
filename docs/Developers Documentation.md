# Developer Documentation for Expense Tracker Project

## Table of Contents
1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Installation and Setup](#installation-and-setup)
4. [In-code Documentation](#in-code-documentation)
5. [User Interaction and Flow](#user-interaction-and-flow)
6. [Known Issues](#known-issues)
7. [Future Work](#future-work)
8. [Ongoing Deployment/Development](#ongoing-deploymentdevelopment)

## Overview
The Expense Tracker project is a simple application to help users manage and track their expenses. Users can add, view, summarize, and delete expenses, as well as view summaries by category. This documentation provides an in-depth guide for developers to understand the project structure, codebase, and workflow.

## Project Structure
Here is a brief overview of the directory structure:

ExpenseTracker/
│
├── docs/
│ ├── review Doc.md
│ ├── spec.md
│ ├── Developer_Documentation.md
│
├── src/
│ ├── expense_tracker.py
│ ├── expenses.py
│
├── requirements.txt
├── README.md
└── LICENSE


- **docs/**: Contains user and developer documentation.
- **src/**: Contains the main application code and modules.
- **tests/**: Contains unit tests for the application.
- **requirements.txt**: Lists the dependencies required for the project.
- **README.md**: Provides an overview and instructions for users.
- **LICENSE**: Contains the license information for the project.

## Installation and Setup
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/ExpenseTracker.git
    cd ExpenseTracker
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```bash
    python src/main.py
    ```

## In-code Documentation
Each module, class, and function in the codebase is documented with docstrings. Below is an overview of the key modules and their functionalities:

- **main.py**: The entry point of the application. It contains the main loop and handles user input for different tasks.
- **expense_manager.py**: Contains the `ExpenseManager` class which handles adding, viewing, and summarizing expenses.
- **file_handler.py**: Contains functions for saving and loading expenses to and from files.
- **expense.py**: Defines the `Expense` class representing an individual expense.
- **utils.py**: Contains utility functions used across the application, such as formatting text.

## User Interaction and Flow
The application provides a menu-driven interface. Below is a brief recap of the user interaction flow:

- **Main Menu:**
    - Add an expense to a new file
    - Summarize a file by category
    - Add an expense to an existing file
    - View the content of a file
    - Delete a file
    - Summarize all files by category
    - Exit

### Code Walkthrough
When the application starts, the user is presented with the main menu. Depending on the user’s choice, the corresponding function is called:

- **Adding an expense to a new file:**
    - `main.py`: `add_expense_to_new_file()`
    - `expense_manager.py`: `ExpenseManager.add_expense()`
    - `file_handler.py`: `save_expense_to_file()`

- **Summarizing a file by category:**
    - `main.py`: `summarize_file()`
    - `expense_manager.py`: `ExpenseManager.summarize_expenses()`

- **Adding an expense to an existing file:**
    - `main.py`: `add_expense_to_existing_file()`
    - `expense_manager.py`: `ExpenseManager.add_expense()`
    - `file_handler.py`: `load_expense_from_file()`, `save_expense_to_file()`

- **Viewing the content of a file:**
    - `main.py`: `view_file_content()`
    - `file_handler.py`: `load_expense_from_file()`

- **Deleting a file:**
    - `main.py`: `delete_file()`
    - `file_handler.py`: `list_expenses()`

- **Summarizing all files by category:**
    - `main.py`: `summarize_all_files()`
    - `expense_manager.py`: `ExpenseManager.summarize_all_expenses()`

## Known Issues

### Minor Issues
- **Error handling:** Input validation could be improved, particularly for numerical inputs.

### Major Issues
- **File operations:** Concurrent access to the same file may cause issues.

## Future Work

### Enhancements
- Implement a graphical user interface (GUI).
- Add support for exporting summaries to CSV or PDF.
- Integrate with external APIs for currency conversion.

### Performance Improvements
- Optimize file operations for large datasets.

## Ongoing Deployment/Development
- **Unit Tests:** Ensure all new features are covered by unit tests in the `tests/` directory.
- **Code Reviews:** Regularly review code to maintain quality and consistency.
- **Documentation:** Keep the documentation updated with any new changes or features.
- **Version Control:** Use semantic versioning for releases to keep track of changes and updates.
