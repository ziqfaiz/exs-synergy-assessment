from datetime import date, timedelta

class User:
    def __init__(self, id, name, address, contact, books=[], penalty=0):
        self._id = id
        self._name = name
        self._address = address
        self._contact = contact
        self._books = []
        self._penalty = penalty

    # define the getters
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

    @property
    def contact(self):
        return self._contact

    @property
    def books(self):
        return self._books

    @property
    def penalty(self):
        return self._penalty

    # define the setters
    @id.setter
    def id(self, value):
        self._id = value

    @name.setter
    def name(self, value):
        self._name = value

    @address.setter
    def address(self, value):
        self._address = value

    @contact.setter
    def contact(self, value):
        self._contact = value

    @books.setter
    def book(self, value):
        self._books.append(value)

    @penalty.setter
    def penalty(self, value):
        self._penalty = value

    def calculate_total_penalty(self):
        total = 0
        for book in self._books:
            total += book.calculate_penalty()
        self._penalty = total
        return total

    def add_book(self, book):
        self._books.append(book)


class Book:
    def __init__(
        self,
        title,
        author,
        id,
        rent_date=date.today(),
        due_date=date.today() + timedelta(days=7),
    ):
        self._title = title
        self._author = author
        self._id = id
        self._rent_date = rent_date
        self._due_date = due_date

    # define the getters
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def id(self):
        return self._id

    @property
    def rent_date(self):
        return self._rent_date

    @property
    def due_date(self):
        return self._due_date

    # define the setters
    @title.setter
    def title(self, value):
        self._title = value

    @author.setter
    def author(self, value):
        self._author = value

    @id.setter
    def id(self, value):
        self._id = value

    @rent_date.setter
    def rent_date(self, value):
        self._rent_date = value

    @due_date.setter
    def due_date(self, value):
        self._due_date = value

    def calculate(self,amount, days):
        return amount * days


    def calculate_penalty(self) -> float:
        total_late = date.today() - self.due_date
        total_late = total_late.days

        if total_late<5:
            return 0
        elif  total_late <= 7:
            return self.calculate(2, total_late-5)

        elif total_late <= 14:
            return self.calculate(3.5, total_late - 7) + self.calculate(2, 2)

        elif total_late <= 30:
            return self.calculate(4, total_late - 14) + self.calculate(3.5, 7) + self.calculate(2, 2)

        elif total_late > 30:
            return (
                self.calculate(5, total_late - 30)
                + self.calculate(4, 16)
                + self.calculate(3.5, 7)
                + self.calculate(2, 2)
            )

        else:
            return 0
