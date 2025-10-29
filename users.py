from abc import ABC


class User(ABC):
    def __init__(self, name, email, phone, password, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.address = address


class Customer(User):
    def __init__(self, name, email, phone, password, address):
        super().__init__(name, email, phone, password, address)
