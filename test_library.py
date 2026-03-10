import pytest
from library import Library, Book

def test_add_and_checkout():
    lib = Library()
    lib.add_book(Book("1984", "George Orwell"))
    assert lib.checkout_book("1984") == "Checked out 1984"

def test_double_checkout_prevention():
    """THIS TEST SHOULD FAIL until the agent fixes library.py"""
    lib = Library()
    lib.add_book(Book("The Hobbit", "J.R.R. Tolkien"))
    
    lib.checkout_book("The Hobbit")
    # This second checkout should return an error or False, not success
    result = lib.checkout_book("The Hobbit")
    
    assert "already checked out" in result.lower() or result == "Book not available"