from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative model
Base = declarative_base()

class Book(Base):
    """
    Book model to represent the books table in the database.
    """
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    published_date = Column(Date, nullable=False)
    isbn = Column(String(13), unique=True, nullable=False)
    pages = Column(Integer, nullable=False)
    cover_url = Column(String(255), nullable=True)
    language = Column(String(2), nullable=False)

    def __init__(self, title, author, published_date, isbn, pages, cover_url, language):
        self.title = title
        self.author = author
        self.published_date = published_date
        self.isbn = isbn
        self.pages = pages
        self.cover_url = cover_url
        self.language = language

    def to_dict(self):
        """Convert the Book instance to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'published_date': self.published_date.isoformat(),
            'isbn': self.isbn,
            'pages': self.pages,
            'cover_url': self.cover_url,
            'language': self.language
        }