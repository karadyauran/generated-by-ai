import sys
from src.services.transaction_service import TransactionService
from src.services.budget_service import BudgetService
from src.utils.helpers import print_menu, get_user_choice, validate_transaction_input

class CLI:
    """
    Command-line interface for interacting with the personal finance tracker.
    """

    def __init__(self, db_connection):
        self.transaction_service = TransactionService(db_connection)
        self.budget_service = BudgetService(self.transaction_service)
        self.main_menu_options = [
            "Add Transaction",
            "View Transactions",
            "Add/Edit Budget",
            "View Budget Report",
            "Exit"
        ]

    def main_menu(self):
        """
        Display the main menu and handle user choices.
        """
        while True:
            print("\nMain Menu")
            print_menu(self.main_menu_options)
            choice = get_user_choice(len(self.main_menu_options))

            if choice == 1:
                self.add_transaction()
            elif choice == 2:
                self.view_transactions()
            elif choice == 3:
                self.add_or_edit_budget()
            elif choice == 4:
                self.view_budget_report()
            elif choice == 5:
                sys.exit()

    def add_transaction(self):
        """
        Add a new transaction.
        """
        print("\nAdd a new Transaction:")
        id_ = validate_transaction_input("Enter transaction ID: ")
        date_str = input("Enter date (YYYY-MM-DD): ")
        amount = validate_transaction_input("Enter amount: ", float)
        category = input("Enter category: ")
        description = input("Enter description (optional): ")

        transaction = Transaction(id=id_, date=date_str, amount=amount, category=category, description=description)
        if transaction.is_valid():
            self.transaction_service.add_transaction(transaction)
            print("Transaction added successfully!")
        else:
            print("Failed to add transaction. Check inputs.")

    def view_transactions(self):
        """
        Display all transactions.
        """
        print("\nTransactions:")
        transactions = self.transaction_service.get_all_transactions()
        for transaction in transactions:
            print(transaction)

    def add_or_edit_budget(self):
        """
        Add or edit budget for a given category.
        """
        print("\nAdd or Edit Budget:")
        category = input("Enter category: ")
        limit = validate_transaction_input("Enter budget limit: ", float)
        self.budget_service.add_budget(category, limit)
        print(f"Budget set for category: {category} with limit {limit}")

    def view_budget_report(self):
        """
        Display budget report for all categories.
        """
        print("\nBudget Report:")
        reports = self.budget_service.get_budget_report()
        for report in reports:
            print(report)