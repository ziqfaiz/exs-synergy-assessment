from database import *
from datetime import date, timedelta

book1 = Book(
    "book1",
    "Joe",
    123,
    date.fromisoformat("2024-07-01"),
    date.fromisoformat("2024-07-15"),
)

book2 = Book(
    "book2",
    "Ali",
    456,
    date.fromisoformat("2024-07-01"),
    date.fromisoformat("2024-07-07"),
)

book3 = Book(
    "book3",
    "James",
    789,
    date.fromisoformat("2024-07-01"),
    date.fromisoformat("2024-07-01"),
)

users = []
user1 = User(1, "user1", "KL", "000")
user1.add_book(book1)
users.append(user1)

user2 = User(2, "user2", "Cyberjaya", "111")
user2.add_book(book2)
user2.add_book(book3)
users.append(user2)

print("Users:")
for user in users:
    print(f"ID: {user.id}")
    for book in user.books:
        print(book.title)

print(f"{user1.penalty}")
user1.calculate_total_penalty()
print(user1.penalty)

print(f"{user2.penalty}")
user2.calculate_total_penalty()
print(user2.penalty)

# generate a list of userss where due date> today
print(f"Users with exxpired due date:")
for user in users:
    for book in user.books:
        if book.due_date < date.today():
            print(f"{user.id} {user.name}")
            print(f"{book.id} {book.title}")
