from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Create a base class for declarative model
Base = declarative_base()

class User(Base):
    """
    User model to represent the users table in the database.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(150), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    registered_on = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, username, email, hashed_password):
        self.username = username
        self.email = email
        self.hashed_password = hashed_password

    def to_dict(self):
        """Convert the User instance to a dictionary."""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'registered_on': self.registered_on.isoformat()
        }