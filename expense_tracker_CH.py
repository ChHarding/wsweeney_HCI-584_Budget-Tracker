from expenses import Expense
import pickle # to save and load data
import os


def get_user_expense():
    print(f"Getting User Expense")
    expense_name = input("What did you buy?")
    expense_amount = float(input("How much did it cost?"))
    expense_categories = ["🍽️ Food", "💸 Bills", "💼 Work", "💳 Debt", "🎉 Fun", "✨ Misc"]
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"    {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range (len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid category. Please try again!")

def save_expense_to_file(expense_list, date):
    filename = f"expenses_{date}.pkl"
    print(f"Saving User Expense for {date} to File")
    with open(filename, "wb+") as f:
        pickle.dump(expense_list, f)

def summarize_expenses(expense_list):
    # this is where it would be handy to have that date be an attribute of Expense ....
    total_expense = 0
    for expense in expense_list:
        print(expense)
        total_expense += expense.amount
    print(f"Total expenses: {total_expense}")

def load_expense_from_file(filename):
    with open(filename, "rb") as f:
        expense_list = pickle.load(f)
    return expense_list

def list_expenses():
    # list all pickel files in the current directory
    expense_dates = []
    files = os.listdir()
    for file in files:
        if file.endswith(".pkl"):
            expense_dates.append(file)
    return expense_dates

def main():

    expense_list = []
    print(f"Running Expense Tracker!")

    date = input("Enter the date (mm-dd-yyyy) of the expenses: ") # should check that it's of that format!

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
    summarize_expenses(expense_list)

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
        summarize_expenses(expense_list)
    
    
    pass # WTH?


if __name__ == "__main__":
    main()
