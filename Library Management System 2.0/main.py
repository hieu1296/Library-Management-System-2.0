class User:
    def __init__(self, name, role):
     
        self.name = name
        self.role = role

    def __str__(self):
        return "ddd"

user = User('dat', 'dat')
print(user)