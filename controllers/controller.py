from app import app
from flask import render_template, request, redirect
from models.books import *
from models.Book import *


@app.route('/books')
def index():
    return render_template('index.jinja', title='Leondale Library', books=books)


@app.route('/books', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    # checked_out = True if 'checked_out' in request.form else False

    new_book = Book(title, author, genre)
    add_new_book(new_book)
    return redirect('/books')


@app.route('/books/delete/<title>', methods=['POST'])
def delete(title):
    delete_book(title)
    return redirect('/books')


@app.route('/books/<index>')
def display_book(index):
    book_to_display = books[int(index)]
    return render_template('book.jinja', book=book_to_display)
