from abc import ABC


class User(ABC):
    def __init__(self, name, email, phone, password, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.address = address


class Seller(User):
    def __init__(self, name, email, phone, password, address):
        super().__init__(name, email, phone, password, address)

    def add_products(self, shop, product_item):
        shop.product.add_products(product_item)


class Customer(User):
    def __init__(self, name, email, phone, password, address):
        super().__init__(name, email, phone, password, address)

    def __repr__(self) -> str:
        return f"<Customer {self.name} ({self.email})>"


# c1 = Customer("Kevin", "k@email.com", 4534324, "1234", "address")
# print(c1)
