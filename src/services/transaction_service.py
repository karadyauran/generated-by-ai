from src.domain.transactions import Transaction
from src.adapters.database import execute_query, fetch_all

class TransactionService:
    """
    Service class to manage and process transactions.
    """

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def add_transaction(self, transaction: Transaction):
        """
        Add a transaction to the database.
        :param transaction: A Transaction instance.
        """
        sql = '''
        INSERT INTO transactions(id, date, amount, category, description)
        VALUES(?, ?, ?, ?, ?)
        '''
        execute_query(self.db_connection, sql, (
            transaction.id,
            transaction.date,
            transaction.amount,
            transaction.category,
            transaction.description
        ))

    def get_all_transactions(self):
        """
        Retrieve all transactions from the database.
        :return: List of Transaction instances.
        """
        sql = '''SELECT id, date, amount, category, description FROM transactions'''
        rows = fetch_all(self.db_connection, sql)
        return [Transaction.from_dict({
            'id': row[0],
            'date': row[1],
            'amount': row[2],
            'category': row[3],
            'description': row[4]
        }) for row in rows]

    def get_transactions_by_category(self, category: str):
        """
        Retrieve transactions filtered by category.
        :param category: The category name.
        :return: List of Transaction instances.
        """
        sql = '''SELECT id, date, amount, category, description FROM transactions WHERE category = ?'''
        rows = fetch_all(self.db_connection, sql, (category,))
        return [Transaction.from_dict({
            'id': row[0],
            'date': row[1],
            'amount': row[2],
            'category': row[3],
            'description': row[4]
        }) for row in rows]

    def total_spent_per_category(self, category: str) -> float:
        """
        Calculate the total amount spent in a specific category.
        :param category: The category name.
        :return: Total spent amount.
        """
        transactions = self.get_transactions_by_category(category)
        return sum(transaction.amount for transaction in transactions)