"""
Price Expense Tracker
"""

import csv
from datetime import datetime

# File names
categories_file = "Database/categories.csv"
expenses_file = "Database/expenses.csv"
balance_file = "Database/balance.csv"


# Function to add a new category
def add_category():
    category = input("Enter a new category: ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    try:
        with open(categories_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([category])
            print(f"Category '{category}' added successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


# Function to add an expense
def add_expense():
    list_categories()  # Display available categories
    category_choice = input("Choose a category by number or enter a new one: ").strip()

    try:
        # Check if the user entered a number
        if category_choice.isdigit():
            with open(categories_file, mode='r') as file:
                categories = list(csv.reader(file))
            category_index = int(category_choice) - 1
            if 0 <= category_index < len(categories):
                category = categories[category_index][0]
            else:
                print("Invalid choice.")
                return
        else:
            # Assume the user wants to add a new category
            category = category_choice
            add_category()

        amount = input("Enter the amount: ").strip()
        subtract_balance(amount)
        if not amount.isdigit():
            print("Amount must be a number.")
            return

        expense = {
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Category": category,
            "Amount": amount,
        }

        with open(expenses_file, mode='a', newline='') as file:
            fieldnames = ["Date", "Category", "Amount"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if file.tell() == 0:  # Write header if file is empty
                writer.writeheader()
            writer.writerow(expense)
            print("Expense added successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


# Function to list all categories
def list_categories():
    try:
        with open(categories_file, mode='r') as file:
            reader = csv.reader(file)
            categories = list(reader)
            if categories:
                print("Available Categories:")
                for i, row in enumerate(categories, 1):
                    print(f"{i}. {row[0]}")
            else:
                print("No categories found. Add some first!")
    except FileNotFoundError:
        print("No categories file found. Add some categories first!")
    except Exception as e:
        print(f"An error occurred: {e}")


def list_expenses():
    currency = " BGN"  # Set your desired currency symbol here
    try:
        with open(expenses_file, mode='r') as file:
            reader = csv.DictReader(file)
            expenses = list(reader)
            if expenses:
                print("\nExpenses:")
                print("{:<15} {:<20} {:<15}".format("Date", "Category", "Amount"))
                print("-" * 50)
                for row in expenses:
                    amount_with_currency = f"{row['Amount']}{currency}"
                    print("{:<15} {:<20} {:<15}".format(row["Date"], row["Category"], amount_with_currency))
            else:
                print("No expenses found. Add some first!")
    except FileNotFoundError:
        print("No expenses file found. Add some expenses first!")
    except Exception as e:
        print(f"An error occurred: {e}")


def read_balance():
    try:
        with open(balance_file, mode='r') as file:
            reader = csv.reader(file)
            curr_balance = float(next(reader)[0])
    except FileNotFoundError:
        print("No balance file found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return curr_balance


def write_balance(curr_balance):
    try:
        with open(balance_file, mode='w') as file:
            writer = csv.writer(file)
            writer.writerow([curr_balance])
    except FileNotFoundError:
        print("No balance file found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def check_balance():
    print(f"Your Current Balance is: {read_balance()}")


def reset_balance():
    print(f"Your Current Balance is: {read_balance()}")
    print("What do you want you new balance to be?")
    new_balance = input("Enter Amount: ")
    write_balance(new_balance)


def subtract_balance(amount):
    curr_balance = read_balance() - float(amount)
    write_balance(curr_balance)
    print(f"New Balance: {read_balance()}")


def add_balance():
    curr_balance = read_balance()
    try:
        while True:
            new_balance = input(f"Current Balance: {curr_balance}! What amount do you want to add to your account: ")
            if new_balance.isdigit():
                curr_balance += float(new_balance)
                break
            else:
                print("Error! Wrong Value! Try a number.")

        write_balance(curr_balance)
        print("Successfully added!")
        print(f"New Balance: {curr_balance}")

    except FileNotFoundError:
        print("No balance file found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def balance():
    while True:
        print("\nMenu:")
        print("1. Check Balance")
        print("2. Reset Balance")
        print("3. Add to Balance")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            check_balance()
        elif choice == "2":
            reset_balance()
        elif choice == "3":
            add_balance()
        else:
            break


# Menu system
def menu():
    while True:
        print("\nMenu:")
        print("1. Add Category")
        print("2. List Categories")
        print("3. Add Expense")
        print("4. List Expenses")
        print("5. Add/Check Balance")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_category()
        elif choice == "2":
            list_categories()
        elif choice == "3":
            add_expense()
        elif choice == "4":
            list_expenses()
        elif choice == "5":
            balance()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    menu()
