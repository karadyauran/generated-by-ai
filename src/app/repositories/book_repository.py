from sqlalchemy.orm import Session
from app.models.book_model import Book

class BookRepository:
    """
    Repository for handling database operations related to books.
    """

    def __init__(self, session: Session):
        self.session = session

    def get_all_books(self):
        """Retrieve all books from the database."""
        return self.session.query(Book).all()

    def get_book_by_id(self, book_id: int):
        """Retrieve a book by its ID."""
        return self.session.query(Book).filter(Book.id == book_id).first()

    def add_book(self, book_data: dict):
        """Add a new book to the database."""
        new_book = Book(**book_data)
        self.session.add(new_book)
        self.session.commit()
        return new_book

    def update_book(self, book_id: int, book_data: dict):
        """Update an existing book's information."""
        book = self.get_book_by_id(book_id)
        if book:
            for key, value in book_data.items():
                setattr(book, key, value)
            self.session.commit()
        return book

    def delete_book(self, book_id: int):
        """Delete a book from the database."""
        book = self.get_book_by_id(book_id)
        if book:
            self.session.delete(book)
            self.session.commit()
            return True
        return False