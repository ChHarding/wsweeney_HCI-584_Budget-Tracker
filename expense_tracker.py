from expense import Expense
import calendar
import datetime
import pickle  # to save and load data
import os


def main():
    print(f"🎯 Running Expense Tracker!")

    date = input("Enter the date (mm-dd-yyyy) of the expenses: ")  # should check that it's of that format!
    expense_list = []

    # Get user input for expense
    while True:
        expense = get_user_expense()
        print(expense)
        expense_list.append(expense)
        yn = input("Do you want to add another expense? (y/n): ")
        if yn.lower() != "y":
            break

    # Write their expense to a file
    save_expense_to_file(expense_list, date)

    # Summarize expenses in list
    summarize_expenses_list(expense_list)

    # List all existing expenses
    expense_dates = list_expenses()
    print("Existing expenses:")
    for i, date in enumerate(expense_dates):
        print(f"{i + 1}. {date}")

    # Load and summarize expenses for a specific date
    selected_index = int(input(f"Summarize? Enter a date number [1 - {len(expense_dates)}]: ")) - 1

    if selected_index in range(len(expense_dates)):
        filename = expense_dates[selected_index]
        expense_list = load_expense_from_file(filename)
        summarize_expenses_list(expense_list)


def get_user_expense():
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
    filename = f"expenses_{date}.pkl"
    print(f"🎯 Saving User Expense for {date} to File")
    with open(filename, "wb+") as f:
        pickle.dump(expense_list, f)


def summarize_expenses_list(expense_list):
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
    with open(filename, "rb") as f:
        expense_list = pickle.load(f)
    return expense_list


def list_expenses():
    # list all pickle files in the current directory
    expense_dates = []
    files = os.listdir()
    for file in files:
        if file.endswith(".pkl"):
            expense_dates.append(file)
    return expense_dates


def green(text):
    return f"\033[92m{text}\033[0m"


if __name__ == "__main__":
    main()
