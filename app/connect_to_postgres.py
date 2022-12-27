import psycopg2
import pandas as pd

def connect_to_postgres(sql_statement):
	conn = psycopg2.connect (
    os.environ['DATABASE_URL'],
    sslmode = 'require',
  )
  df = pd.read_sql_query(sql_statement, con=conn)
  conn.close()
  return df

"""

import pandas as pd
from app import db
df = pd.read_sql(<YOUR-SQL-QUERY>, db.session.bind)

from app import db
db.session.bind.execute(<YOUR-SQL-STATEMENT>)

from sqlalchemy import func
from app.models import Book
from flask import request

@app.route('/searchTitles', methods=['POST'])
def search_titles():
	search = request.form['search'] # find the input in the form your user sent
	search = search.lower()
	filtered_books = Book.query.filter(func.lower(Book.title).like(f'%{search}%')).all()
  return # format and then render the book list
  
https://docs.sqlalchemy.org/en/14/core/functions.html

"""
