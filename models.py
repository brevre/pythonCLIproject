from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    
    # Relationship
    borrowed_books = relationship("Transaction", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    available = Column(Boolean, default=True)

    def __repr__(self):
        return f"Book(id={self.id}, title={self.title}, author={self.author}, available={self.available})"

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))

    user = relationship("User", back_populates="borrowed_books")
    book = relationship("Book")

    def __repr__(self):
        return f"Transaction(id={self.id}, user_id={self.user_id}, book_id={self.book_id})"
