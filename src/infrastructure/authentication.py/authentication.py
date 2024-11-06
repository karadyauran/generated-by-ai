import hashlib
import os
import json

class Authentication:
    """
    Handles user authentication by managing username and password storage.
    """

    def __init__(self, filename: str):
        """
        Initialize the Authentication with a filename for storing authentication data.

        :param filename: The name of the file where authentication data is stored.
        """
        self.filename = filename

    def register_user(self, username: str, password: str):
        """
        Register a new user with a username and password.

        :param username: Username for the new user.
        :param password: Password for the new user.
        """
        hashed_password = self._hash_password(password)
        auth_data = self._load_auth_data()

        if username in auth_data:
            raise ValueError("Username already exists.")

        auth_data[username] = hashed_password
        self._save_auth_data(auth_data)

    def authenticate_user(self, username: str, password: str) -> bool:
        """
        Authenticate a user with their username and password.

        :param username: Username of the user.
        :param password: Password of the user.
        :return: True if authentication is successful, False otherwise.
        """
        auth_data = self._load_auth_data()
        hashed_password = auth_data.get(username)

        return hashed_password is not None and hashed_password == self._hash_password(password)

    def _hash_password(self, password: str) -> str:
        """
        Hash a password for secure storage.

        :param password: Password to be hashed.
        :return: The hashed representation of the password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def _load_auth_data(self) -> dict:
        """
        Load authentication data from the file.

        :return: A dictionary with username and hashed passwords.
        """
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _save_auth_data(self, auth_data: dict):
        """
        Save the authentication data to the file.

        :param auth_data: A dictionary with usernames and hashed passwords.
        """
        with open(self.filename, 'w') as file:
            json.dump(auth_data, file, indent=4)