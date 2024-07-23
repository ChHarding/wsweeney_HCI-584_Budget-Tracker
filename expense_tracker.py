from expenses import Expense  # Corrected import statement
import calendar
import datetime
import pickle  # to save and load data
import os

def main():
    """Main function to run the Expense Tracker application."""
    print(f"🎯 Running Expense Tracker!")

    while True:
        print("Select a task:")
        print("1. Add an expense to a new file")
        print("2. Summarize a file by category")
        print("3. Add an expense to an existing file")
        print("4. View the content of a file")
        print("5. Delete a file")
        print("6. Summarize all files by category")
        print("7. Exit")

        task = input("Pick a task (1 - 7): ")

        if task == "1":
            add_expense_to_new_file()
        elif task == "2":
            summarize_file()
        elif task == "3":
            add_expense_to_existing_file()
        elif task == "4":
            view_file_content()
        elif task == "5":
            delete_file()
        elif task == "6":
            summarize_all_files()
        elif task == "7":
            break
        else:
            print("Invalid task. Please try again!")

def add_expense_to_new_file():
    """Add a new expense to a new file."""
    date = input("Enter the date (mm-dd-yyyy) of the expenses: ")  # should check that it's of that format!
    expense_list = []

    while True:
        expense = get_user_expense()
        print(expense)
        expense_list.append(expense)
        yn = input("Do you want to add another expense? (y/n): ")
        if yn.lower() != "y":
            break

    save_expense_to_file(expense_list, date)

def summarize_file():
    """Summarize the expenses of a selected file by category."""
    expense_dates = list_expenses()
    print("Existing expenses:")
    for i, date in enumerate(expense_dates):
        print(f"{i + 1}. {date}")

    selected_index = int(input(f"Summarize? Enter a date number [1 - {len(expense_dates)}]: ")) - 1

    if selected_index in range(len(expense_dates)):
        filename = expense_dates[selected_index]
        expense_list = load_expense_from_file(filename)
        summarize_expenses_list(expense_list)

def add_expense_to_existing_file():
    """Add a new expense to an existing file."""
    expense_dates = list_expenses()
    print("Existing expenses:")
    for i, date in enumerate(expense_dates):
        print(f"{i + 1}. {date}")

    selected_index = int(input(f"Add to which file? Enter a date number [1 - {len(expense_dates)}]: ")) - 1

    if selected_index in range(len(expense_dates)):
        filename = expense_dates[selected_index]
        expense_list = load_expense_from_file(filename)

        while True:
            expense = get_user_expense()
            print(expense)
            expense_list.append(expense)
            yn = input("Do you want to add another expense? (y/n): ")
            if yn.lower() != "y":
                break

        save_expense_to_file(expense_list, filename)

def view_file_content():
    """View the content of a selected file."""
    expense_dates = list_expenses()
    print("Existing expenses:")
    for i, date in enumerate(expense_dates):
        print(f"{i + 1}. {date}")

    selected_index = int(input(f"View which file? Enter a date number [1 - {len(expense_dates)}]: ")) - 1

    if selected_index in range(len(expense_dates)):
        filename = expense_dates[selected_index]
        expense_list = load_expense_from_file(filename)
        for expense in expense_list:
            print(expense)

def delete_file():
    """Delete a selected file."""
    expense_dates = list_expenses()
    print("Existing expenses:")
    for i, date in enumerate(expense_dates):
        print(f"{i + 1}. {date}")

    selected_index = int(input(f"Delete which file? Enter a date number [1 - {len(expense_dates)}]: ")) - 1

    if selected_index in range(len(expense_dates)):
        filename = expense_dates[selected_index]
        os.remove(filename)
        print(f"Deleted {filename}")

def summarize_all_files():
    """Summarize all expenses from all files by category."""
    expense_dates = list_expenses()
    all_expenses = []

    for filename in expense_dates:
        expense_list = load_expense_from_file(filename)
        all_expenses.extend(expense_list)

    summarize_expenses_list(all_expenses)

def get_user_expense():
    """Prompt the user to input details for a new expense.

    Returns:
        Expense: A new Expense object.
    """
    print(f"🎯 Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = ["🍽️  Food", "💸  Bills", "💼 Work", "💳 Debt", "🎉 Fun", "✨ Misc"]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense
        else:
            print("Invalid category. Please try again!")

def save_expense_to_file(expense_list, date):
    """Save the list of expenses to a file.

    Args:
        expense_list (list): The list of Expense objects to save.
        date (str): The date used for naming the file.
    """
    filename = f"expenses_{date}.pkl" if not date.endswith(".pkl") else date
    print(f"🎯 Saving User Expense for {date} to File")
    with open(filename, "wb+") as f:
        pickle.dump(expense_list, f)

def summarize_expenses_list(expense_list):
    """Summarize a list of expenses by category and total amount.

    Args:
        expense_list (list): The list of Expense objects to summarize.
    """
    print(f"🎯 Summarizing User Expense")
    total_expense = 0
    amount_by_category = {}

    for expense in expense_list:
        print(expense)
        total_expense += expense.amount
        if expense.category in amount_by_category:
            amount_by_category[expense.category] += expense.amount
        else:
            amount_by_category[expense.category] = expense.amount

    print("Expenses By Category 📈:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")

    print(f"💵 Total expenses: ${total_expense:.2f}")

    budget = 2000  # Assuming budget is fixed, this can be made dynamic if needed
    remaining_budget = budget - total_expense
    print(f"✅ Budget Remaining: ${remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(green(f"👉 Budget Per Day: ${daily_budget:.2f}"))

def load_expense_from_file(filename):
    """Load a list of expenses from a file.

    Args:
        filename (str): The name of the file to load the expenses from.

    Returns:
        list: The list of Expense objects loaded from the file.
    """
    with open(filename, "rb") as f:
        expense_list = pickle.load(f)
    return expense_list

def list_expenses():
    """List all expense files in the current directory.

    Returns:
        list: A list of filenames for all expense files.
    """
    expense_dates = []
    files = os.listdir()
    for file in files:
        if file.endswith(".pkl"):
            expense_dates.append(file)
    return expense_dates

def green(text):
    """Return text formatted in green.

    Args:
        text (str): The text to format.

    Returns:
        str: The formatted text.
    """
    return f"\033[92m{text}\033[0m"

if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
