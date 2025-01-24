from Enums import AccountStatus
from Book import Book
from datetime import date

class Address:
    def __init__(self, streetAddress: str, city :str, state:str, zipcode:str, country:str):
        self.streetAddress = streetAddress
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.country = country

class Person:
    def __init__(self, name):
        self.name = name

    def getaName(self) ->str:
        return self.name


class Person:
    def __init__(self, name: str):
        self.name = name

class User(Person):
    def __init__(self, id: int, name: str, address: str, email: str, phone: str):
        super().__init__(name)
        self.id = id
        self.address = address
        self.email = email
        self.phone = phone

class Librarian(User):
    def __init__(self, id: int, name: str, address: str, email: str, phone: str):
        super().__init__(id, name, address, email, phone)

    def addBookItem(self, book_id: int, title: str, author: str) -> bool:
        # Implementation for adding a book
        pass

    def blockMember(self, member_id: int) -> bool:
        # Implementation for blocking a member
        pass

    def unblockMember(self, member_id: int) -> bool:
        # Implementation for unblocking a member
        pass

class Member(User):
    def __init__(self, id: int, name: str, address: str, email: str, phone: str, date_of_membership: date, total_books_checked_out: int = 0):
        super().__init__(id, name, address, email, phone)
        self.date_of_membership = date_of_membership
        self.total_books_checked_out = total_books_checked_out

    def getTotalCheckedoutBooks(self) -> int:
        return self.total_books_checked_out

    def canCheckoutBook(self) -> bool:
        return self.total_books_checked_out < 3  


class Account:
    def __init__(self, id: int, password: str, status: AccountStatus, person: User):
        self.id = id
        self.password = password
        self.status = status
        self.person = person

