class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def __repr__(self):
        return f"Book({self.title!r})"


class Library:
    def __init__(self):
        self.books = []
        self.checkouts = []

    def add_book(self, book):
        self.books.append(book)

    def checkout_book(self, book):
        # BUG: no check if book is already checked out
        self.checkouts.append(book)
        book.is_checked_out = True
        return True

    def return_book(self, book):
        if book in self.checkouts:
            self.checkouts.remove(book)
            book.is_checked_out = False
            return True
        return False

    def available_books(self):
        return [b for b in self.books if not b.is_checked_out]