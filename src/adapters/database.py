import sqlite3
from sqlite3 import Connection, Error


def create_connection(db_file) -> Connection:
    """
    Create a database connection to a SQLite database.
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_table(conn: Connection, create_table_sql):
    """
    Create a table from the create_table_sql statement.
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def execute_query(conn: Connection, query, parameters=()):
    """
    Execute a single query.
    :param conn: Connection object
    :param query: The SQL query
    :param parameters: Optional parameters for the query
    """
    try:
        c = conn.cursor()
        c.execute(query, parameters)
        conn.commit()
    except Error as e:
        print(e)


def fetch_all(conn: Connection, query, parameters=()):
    """
    Fetch all results from a query.
    :param conn: Connection object
    :param query: The SQL query
    :param parameters: Optional parameters for the query
    :return: List of tuples with query results
    """
    try:
        c = conn.cursor()
        c.execute(query, parameters)
        return c.fetchall()
    except Error as e:
        print(e)
        return []


def fetch_one(conn: Connection, query, parameters=()):
    """
    Fetch a single result from a query.
    :param conn: Connection object
    :param query: The SQL query
    :param parameters: Optional parameters for the query
    :return: A single tuple with the query result
    """
    try:
        c = conn.cursor()
        c.execute(query, parameters)
        return c.fetchone()
    except Error as e:
        print(e)
        return None
