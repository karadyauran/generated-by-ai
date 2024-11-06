import sqlite3
from typing import List, Dict, Tuple, Any

class DatabaseManager:
    def __init__(self, db_name: str = 'expense_tracker.db'):
        """
        Initializes the database manager and creates the connection.
        :param db_name: Name of the database file
        """
        self.db_name = db_name
        self.connection = self.create_connection()
        self.create_tables()

    def create_connection(self) -> sqlite3.Connection:
        """
        Create a database connection.
        :returns: SQLite Connection object
        """
        try:
            return sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def create_tables(self) -> None:
        """
        Create necessary tables for users and transactions.
        """
        tables = {
            "users": """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                )
            """,
            "transactions": """
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    type TEXT NOT NULL,
                    category TEXT NOT NULL,
                    amount REAL NOT NULL,
                    date TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            """
        }

        cursor = self.connection.cursor()

        for table_name, create_statement in tables.items():
            cursor.execute(create_statement)
        self.connection.commit()

    def execute_query(self, query: str, parameters: Tuple = ()) -> None:
        """
        Execute a write query (INSERT, UPDATE, DELETE)
        :param query: SQL query string
        :param parameters: Parameters for the query
        """
        cursor = self.connection.cursor()
        cursor.execute(query, parameters)
        self.connection.commit()

    def fetch_query(self, query: str, parameters: Tuple = ()) -> List[Dict[str, Any]]:
        """
        Execute a read query (SELECT)
        :param query: SQL query string
        :param parameters: Parameters for the query
        :returns: List of rows as dictionaries
        """
        cursor = self.connection.cursor()
        cursor.execute(query, parameters)
        columns = [column[0] for column in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def close_connection(self) -> None:
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()

# Note: This code will be part of a larger system; ensure your main.py interacts correctly with the database module.