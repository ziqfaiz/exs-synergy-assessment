from database import User, Book
from datetime import timedelta, date


def calculate(amount, days):
    return amount * days


def calculate_penalty(book: Book) -> float:
    total_late = book.due_date - date.today()
    total_late = total_late.days

    if total_late <= 7:
        return calculate(2, total_late - 5)

    elif total_late <= 14:
        return calculate(3.5, total_late - 7) + calculate(2, 2)

    elif total_late <= 30:
        return calculate(4, total_late - 14) + calculate(3.5, 7) + calculate(2, 2)

    elif total_late > 30:
        return (
            calculate(5, total_late - 30)
            + calculate(4, 16)
            + calculate(3.5, 7)
            + calculate(2, 2)
        )

    else:
        return 0
