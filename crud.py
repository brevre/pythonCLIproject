from sqlalchemy.orm import Session
from models import User, Book, Transaction

def add_user(session: Session, name: str, email: str):
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    return user

def add_book(session: Session, title: str, author: str):
    book = Book(title=title, author=author)
    session.add(book)
    session.commit()
    return book

def list_books(session: Session):
    return session.query(Book).all()

def borrow_book(session: Session, user_id: int, book_id: int):
    book = session.query(Book).filter_by(id=book_id, available=True).first()
    if not book:
        return "Book not available"
    
    book.available = False
    transaction = Transaction(user_id=user_id, book_id=book_id)
    session.add(transaction)
    session.commit()
    return transaction

def return_book(session: Session, book_id: int):
    transaction = session.query(Transaction).filter_by(book_id=book_id).first()
    if transaction:
        book = session.query(Book).filter_by(id=book_id).first()
        book.available = True
        session.delete(transaction)
        session.commit()
        return "Book returned"
    return "Transaction not found"
