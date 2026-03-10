from library import Library, Book
from utils import format_book_name

def start_app():
    my_library = Library()
    b1 = Book("Python Crash Course", "Eric Matthes")
    my_library.add_book(b1)
    
    print(format_book_name(b1.title, b1.author))
    print(my_library.checkout_book("Python Crash Course"))

if __name__ == "__main__":
    start_app()