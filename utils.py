def format_book_list(books):
    if not books:
        return "No books available."
    return "\n".join(f"  - {b.title} by {b.author}" for b in books)