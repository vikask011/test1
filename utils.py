def calculate_fines(days_overdue, daily_rate):
    """Calculates fine, but crashes if daily_rate is not provided correctly."""
    return days_overdue / daily_rate

def format_book_name(title, author):
    return f"{title.upper()} by {author.title()}"