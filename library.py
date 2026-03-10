class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def checkout_book(self, title):
        for book in self.books:
            if book.title == title:
                # BUG: Missing check if book.is_available is already False
                book.is_available = False
                return f"Checked out {title}"
        return "Book not found"

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.is_available = True
                return f"Returned {title}"
        return "Book not found"