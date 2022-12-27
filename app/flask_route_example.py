import flask
from flask import render_template
from app.models import Book
from app import app

@app.route('/')
def home():
	return render_template('home.html')


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/book-list')
def book_list():
	books = Book.query.all()
	return render_template(
		'book_list.html',
		books = books,
		n_books = len(books),
		n_rows = int(len(books)/2) + int(len(books)%2==1)
		)
