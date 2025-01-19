class Person:
    def __init__(self, name):
        self.name = name

class Author(Person):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description

class User(Person):
    def __init__(self, id :int , name:str, address: str, email:str, phone:str):
        super().__init__(name)
        self.id = id
        self.address = address
        self.email = email
        self.phone = phone

class Librarian(User):
    def __init__(self, id, name):
        super().__init__(id, name)

    def addBookItem() -> bool:
        pass

    def blockMember():
        pass
    
    def unblockMember():
        pass

class Member(User):
    def __init__(self, id, name, dateOfMembership, totalBooksCheckedout : int):
        super().__init__(id, name)
        self.dateOfMembership = dateOfMembership
        self.totalBooksCheckedout = totalBooksCheckedout

    def getTotalCheckedoutBooks(self) -> int:
        return self.totalBooksCheckedout
    




# if not isinstance(role, UserRole):
#             raise ValueError("Invalid role")
#         self.name = name
#         self.role = role