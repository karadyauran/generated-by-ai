import os
from dotenv import load_dotenv
from src.presentation.cli_interface import CLIInterface

# Load environment variables
load_dotenv()

# Retrieve file paths and user credentials from environment variables
transaction_file = os.getenv("TRANSACTION_FILE", "transactions.json")
auth_file = os.getenv("AUTH_FILE", "auth.json")

# Initialize the CLI Interface
def main():
    cli_interface = CLIInterface(transaction_file, auth_file)

    # Welcome message
    print("Welcome to the Personal Finance Tracker!")

    # User authentication
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if not cli_interface.login(username, password):
        print("Invalid credentials. Please try again.")
        return

    print("Login successful!")

    # Main menu
    while True:
        print("\nMain Menu:")
        print("1. Add Transaction")
        print("2. Set Budget")
        print("3. Display Budgets")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            add_transaction(cli_interface)
        elif choice == '2':
            set_budget(cli_interface)
        elif choice == '3':
            print(cli_interface.display_budgets())
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid menu option.")


# Function to add a new transaction
def add_transaction(cli_interface):
    try:
        amount = float(input("Enter transaction amount: "))
        date = input("Enter transaction date (YYYY-MM-DD): ")
        category = input("Enter transaction category: ")
        description = input("Enter optional description (leave blank if none): ")
        cli_interface.add_transaction(amount, date, category, description)
        print("Transaction added successfully.")
    except ValueError:
        print("Invalid input. Please enter valid data.")


# Function to set a budget
def set_budget(cli_interface):
    try:
        category = input("Enter budget category: ")
        amount = float(input("Enter budget amount: "))
        cli_interface.set_budget(category, amount)
        print("Budget set successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")


if __name__ == "__main__":
    main()
