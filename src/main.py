import sys
from src.adapters.database import create_connection, create_table
from src.interfaces.cli import CLI

DB_FILE = "financial_tracker.db"
TRANSACTIONS_TABLE_SQL = '''
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    description TEXT
);
'''


def main():
    """
    Main entry point for the personal finance tracker application.
    """
    db_connection = create_connection(DB_FILE)  # Establish database connection
    if db_connection is None:
        print("Error! Cannot create the database connection.")
        sys.exit(1)

    create_table(db_connection, TRANSACTIONS_TABLE_SQL)  # Create the transactions table if it doesn't exist

    cli_interface = CLI(db_connection)  # Instantiate the command-line interface
    cli_interface.main_menu()  # Start the main menu loop

    db_connection.close()  # Close the database connection when done


if __name__ == '__main__':
    main()