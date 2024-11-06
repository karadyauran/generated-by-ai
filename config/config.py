# config/config.py
# Configuration module to manage application settings

import os
from dotenv import load_dotenv

class Config:
    """
    A class to manage configuration settings for the application.

    Loads environment variables from a .env file if available.
    """

    def __init__(self):
        # Load environment variables from a .env file if it exists
        load_dotenv()

        # Set configuration variables from environment variables or defaults
        self.debug = self._get_bool_env_variable('DEBUG', default=False)
        self.database_path = os.getenv('DATABASE_PATH', 'data/tasks.db')
        self.log_level = os.getenv('LOG_LEVEL', 'INFO')

    def _get_bool_env_variable(self, key, default=False):
        """
        Get a boolean environment variable.

        Parameters:
        key (str): The name of the environment variable.
        default (bool): The default value if the environment variable is not set.

        Returns:
        bool: The value of the environment variable or the default if not set.
        """
        value = os.getenv(key, str(default))
        return value.lower() in ('true', '1', 't', 'y', 'yes')


# Example Usage
# config = Config()
# print("Debug mode:", config.debug)
# print("Database path:", config.database_path)
# print("Log level:", config.log_level)
