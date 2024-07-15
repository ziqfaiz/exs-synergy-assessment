from database import *
import json


def database_builder():
    database = []

    user1 = User(1, "Ali", "14, WDC, Washington DC", "+6012345678")
    user2 = User(2, "Abu", "14, CA, California", "+6012345611")

    book1 = Book(
        "The Glass Castle",
        "Jeanette Walls",
        123,
        date.fromisoformat("2024-06-27"),
        date.fromisoformat("2024-07-27"),
    )

    book2 = Book(
        "Lion King",
        "Ahmad Albab",
        456,
        date.fromisoformat("2024-07-01"),
        date.fromisoformat("2024-07-07"),
    )

    book3 = Book(
        "Harry Potter",
        "J. K. Rowling",
        789,
        date.fromisoformat("2024-06-01"),
        date.fromisoformat("2024-07-01"),
    )

    book4 = Book(
        "Columbine",
        "Dave Cullen",
        000,
        date.fromisoformat("2024-05-01"),
        date.fromisoformat("2024-06-01"),
    )

    user1.add_book(book1)
    user1.add_book(book2)
    user1.calculate_total_penalty()
    user2.add_book(book3)
    user2.add_book(book4)
    user2.calculate_total_penalty()
    database.append(user1)
    database.append(user2)
    return database
