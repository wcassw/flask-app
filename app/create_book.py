from app.models import Book
from app import db

book = Book(
  title = 'Anna Karenina',
  author_name = 'Leo Tolstoy',
  )
db.session.add(book)
try: db.session.commit()
except: db.session.rollback()

"""

from app import db
from app.models import Book
book = Book.query.filter_by(title = 'Jane Eyre')
book.author_name = 'Charlotte Brontë'
db.session.commit()

https://stackoverflow.com/questions/3659142/bulk-insert-with-sqlalchemy-orm

"""
