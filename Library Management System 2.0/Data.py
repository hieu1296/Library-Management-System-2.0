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




class Address:
    def __init__(self, streetAddress: str, city :str, state:str, zipcode:str, country:str):
        self.streetAddress = streetAddress
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.country = country