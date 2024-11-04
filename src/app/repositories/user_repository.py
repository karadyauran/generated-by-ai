from sqlalchemy.orm import Session
from app.models.user_model import User

class UserRepository:
    """
    Repository for handling database operations related to users.
    """

    def __init__(self, session: Session):
        self.session = session

    def get_all_users(self):
        """Retrieve all users from the database."""
        return self.session.query(User).all()

    def get_user_by_id(self, user_id: int):
        """Retrieve a user by their ID."""
        return self.session.query(User).filter(User.id == user_id).first()

    def add_user(self, user_data: dict):
        """Add a new user to the database."""
        new_user = User(**user_data)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def update_user(self, user_id: int, user_data: dict):
        """Update an existing user's information."""
        user = self.get_user_by_id(user_id)
        if user:
            for key, value in user_data.items():
                setattr(user, key, value)
            self.session.commit()
        return user

    def delete_user(self, user_id: int):
        """Delete a user from the database."""
        user = self.get_user_by_id(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False