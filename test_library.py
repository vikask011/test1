from library import Library, Book


def test_add_and_checkout():
    lib = Library()
    book = Book("Clean Code", "Robert Martin")
    lib.add_book(book)

    result = lib.checkout_book(book)
    assert result == True
    assert book.is_checked_out == True
    assert book not in lib.available_books()


def test_double_checkout_prevention():
    lib = Library()
    book = Book("The Pragmatic Programmer", "Hunt & Thomas")
    lib.add_book(book)

    first = lib.checkout_book(book)
    assert first == True

    # Second checkout of the same book should be rejected
    second = lib.checkout_book(book)
    assert second == False, "Should not allow checking out an already checked-out book"

    # Should only appear once in checkouts
    assert lib.checkouts.count(book) == 1