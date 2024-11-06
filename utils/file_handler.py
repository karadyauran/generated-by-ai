# utils/file_handler.py

import json
import os
from pathlib import Path


class FileHandler:
    """
    FileHandler manages data reading and writing operations to the file system.
    Supports JSON format for data persistence.
    """

    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def read_data(self):
        """
        Reads data from a JSON file and returns it as a Python object.
        Returns an empty list if the file doesn't exist or is empty.
        """
        if not self.file_path.exists():
            return []

        with open(self.file_path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
        return data

    def write_data(self, data):
        """
        Writes a Python object to a file in JSON format.

        Parameters:
        data (iterable): The data to write to the file.
        """
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def ensure_directory_exists(self):
        """
        Ensures the directory for the file_path exists, creates if it does not.
        """
        dir_path = self.file_path.parent
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)


# Example Usage
# handler = FileHandler('data/tasks.json')
# data = handler.read_data()
# handler.write_data(data)