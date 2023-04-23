from models.Book import *

book1 = Book("When the Lion Feeds", "Wilbur Smith", "Adventure", True)
book2 = Book("Pride and Prejudice", "Jane Austen", "Romance", False)
book3 = Book("Lamb to the Slaughter", "Roald Dahl", "Short Story", True)

books = [book1, book2, book3]


def add_new_book(book):
    books.append(book)


def delete_book(book_title):
    book_to_delete = None
    for book in books:
        if book.title == book_title:
            book_to_delete = book
            break

    books.remove(book_to_delete)

# def check_out_book(book):
#     for book in books:
#         if book.title == book_title and not book.checked_out:
#             book.checked_out = True
