from app import db
from sqlalchemy.orm import relationship, Table, Column, Base, Foreignkey

class Item(db.Model):
	__tablename__ = 'items'
	id = db.Column(db.Integer,primary_key=True)


class Book(db.Model):

	__tablename__ = 'book'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(128))
	author_name = db.Column(db.String(64))

	__table_args__ = (
		db.UniqueConstraint('title', 'author_name', name = 'UC_book_author'),
	)


class Subscription(db.Model): 

	__tablename__ = 'subscription'

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(128))
	created_at = db.Column(db.DateTime)
	# reference to book
	book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
	book = db.relationship('Book', backref='book')

	__table_args__ = (
		db.UniqueConstraint('email', 'book_id', name = 'UC_email_book'),
	)

"""
>>> from app.models import Subscription
>>> s = Subscription.query.get(5)
>>> s
<Subscription 5>
>>> s.book
<Book 3>
>>> s.book.title
'The Picture of Dorian Gray'

python manage.py db init
  OR
flask db init

python manage.py db upgrade
  OR
flask db upgrade

heroku run bash
>>> python manage.py db init
>>> python manage.py db migrate
>>> python manage.py db upgrade


"""
