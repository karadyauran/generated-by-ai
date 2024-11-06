from typing import Any, Dict

class User:
    """
    Represents a user of the expense tracking system.
    """
    def __init__(self, user_id: int, username: str, password_hash: str):
        """
        Initialize a user.
        :param user_id: Unique identifier for the user
        :param username: Username of the user
        :param password_hash: Hashed password for security
        """
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the User instance to a dictionary.
        :returns: Dictionary representation of the user
        """
        return {
            'user_id': self.user_id,
            'username': self.username,
            'password_hash': self.password_hash
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'User':
        """
        Create a User instance from a dictionary.
        :param data: Dictionary with user data
        :returns: User instance
        """
        return cls(
            user_id=data.get('user_id', 0),
            username=data['username'],
            password_hash=data['password_hash']
        )

    def __repr__(self) -> str:
        """
        Return the string representation of the user.
        :returns: String representation
        """
        return (f"User(id={self.user_id}, username={self.username})")

    def check_password(self, password: str) -> bool:
        """
        Verify a password against the stored hash.
        :param password: Plain text password
        :returns: True if password matches, else False
        """
        # This function should incorporate actual password verification logic, e.g., using bcrypt
        # Here is a placeholder implementation
        return self.password_hash == password  # Placeholder (for illustration purposes only)
