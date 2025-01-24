from enum import Enum

class AccountStatus(Enum):
    Active = 'Active'
    Closed = 'Closed'
    Canceled = 'Canceled'
    Blacklisted = 'Blacklisted'
    None = 'None'

class ReservaionStatus(Enum):
    Waiting = 'Waiting'
    Pending = 'Pending'
    Completed = 'Completed'
    Canceled = 'Canceled'
    None = 'None'

class BookStatus(Enum):
    Available = 'Available'
    Reserved = 'Reserved'
    Loaned = 'Loaned'
    Lost = 'Lost'

class BookFormat(Enum):
    Hardcover = 'Hardcover'
    Paperback = 'Paperback'
    Audiobook = 'Audiobook'
    Ebook = 'Ebook'
    Newspaper = 'Newspaper'
    Magazine = 'Magazine'
    Journal = 'Journal'
    
class Address:
    def __init__(self, streetAddress: str, city :str, state:str, zipcode:str, country:str):
        self.streetAddress = streetAddress
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.country = country
