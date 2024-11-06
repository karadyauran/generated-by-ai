# utils/date_manager.py

from datetime import datetime

class DateManager:
    """
    DateManager provides utility functions for handling date operations.
    Includes formatting and comparison of dates.
    """

    def __init__(self, date_format='%Y-%m-%d'):
        """
        Initializes the DateManager with a date format.

        Parameters:
        date_format (str): The format in which dates should be processed and displayed.
        """
        self.date_format = date_format

    def parse_date(self, date_str):
        """
        Parses a string into a datetime object according to the specified format.

        Parameters:
        date_str (str): The date string to parse.

        Returns:
        datetime: Parsed date as a datetime object.
        """
        try:
            return datetime.strptime(date_str, self.date_format)
        except ValueError:
            raise ValueError(f"Invalid date format. Expected {self.date_format}.")

    def format_date(self, date):
        """
        Formats a datetime object to a string according to the specified format.

        Parameters:
        date (datetime): The date to format.

        Returns:
        str: The formatted date string.
        """
        return date.strftime(self.date_format)

    def compare_dates(self, date1, date2):
        """
        Compares two dates and returns:
        -1 if date1 < date2,
         0 if date1 == date2,
         1 if date1 > date2.

        Parameters:
        date1 (datetime): First date for comparison.
        date2 (datetime): Second date for comparison.

        Returns:
        int: Comparison result.
        """
        if date1 < date2:
            return -1
        elif date1 > date2:
            return 1
        else:
            return 0
