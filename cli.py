import click
from database import SessionLocal
from crud import add_user, add_book, list_books, borrow_book, return_book

@click.group()
def cli():
    """Library CLI"""
    pass

@click.command()
@click.argument("name")
@click.argument("email")
def register(name, email):
    """Register a new user"""
    session = SessionLocal()
    user = add_user(session, name, email)
    click.echo(f"User registered: {user}")

@click.command()
@click.argument("title")
@click.argument("author")
def addbook(title, author):
    """Add a new book"""
    session = SessionLocal()
    book = add_book(session, title, author)
    click.echo(f"Book added: {book}")

@click.command()
def books():
    """List all books"""
    session = SessionLocal()
    books = list_books(session)
    for book in books:
        click.echo(book)

@click.command()
@click.argument("user_id", type=int)
@click.argument("book_id", type=int)
def borrow(user_id, book_id):
    """Borrow a book"""
    session = SessionLocal()
    result = borrow_book(session, user_id, book_id)
    click.echo(result)

@click.command()
@click.argument("book_id", type=int)
def returnbook(book_id):
    """Return a borrowed book"""
    session = SessionLocal()
    result = return_book(session, book_id)
    click.echo(result)

cli.add_command(register)
cli.add_command(addbook)
cli.add_command(books)
cli.add_command(borrow)
cli.add_command(returnbook)

if __name__ == "__main__":
    cli()
