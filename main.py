from library import Library, Book


def main():
    lib = Library()

    books = [
        Book("Clean Code", "Robert Martin"),
        Book("The Pragmatic Programmer", "Hunt & Thomas"),
        Book("Design Patterns", "Gang of Four"),
    ]

    for book in books:
        lib.add_book(book)

    print("Available books:", lib.available_books())

    lib.checkout_book(books[0])
    print("After checkout:", lib.available_books())

    lib.return_book(books[0])
    print("After return:", lib.available_books())


if __name__ == "__main__":
    main()