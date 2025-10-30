from abc import ABC
from orders import Order
from product import ProductItem


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

    def remove_product(self, shop, product_item):
        shop.product.remove_product(product_item)

    def show_products(self, shop):
        shop.product.show_products()


class Customer(User):
    def __init__(self, name, email, phone, password, address):
        super().__init__(name, email, phone, password, address)
        self.cart = Order()

    def view_all_products(self, shop):
        shop.product.show_products()

    def add_product_to_cart(self, shop, product_name, quantity):
        pr = shop.product.find_product(product_name)
        if pr:
            if pr.quantity >= quantity:
                pr.quantity -= quantity

                cart_item = ProductItem(pr.name, pr.price, quantity)

                self.cart.add_product_item(cart_item, quantity)
                print(f"{quantity} x {pr.name} added to the cart")

            else:
                print("Not enough stock available")
        else:
            print("Product not found")

    def remove_product_from_cart(self, shop, product_name, quantity):
        found = False
        for product in list(self.cart.product_items.keys()):
            if product.name.lower() == product_name.lower():
                found = True
                if quantity <= self.cart.product_items[product]:
                    shop_product = shop.product.find_product(product_name)

                    if shop_product:
                        shop_product.quantity += quantity

                    self.cart.product_items[product] -= quantity

                    if self.cart.product_items[product] == 0:
                        del self.cart.product_items[product]
                        print(f"{product.name} removed from the cart")
                    else:
                        print(f"Removed {quantity} of {product.name} from the cart")
                else:
                    print("\nYou do not have that many items in your cart")
                break
        if not found:
            print("\nProduct not found in your cart")

    def view_cart(self):
        print("\n---View Cart---")
        if not self.cart.product_items:
            print("\nYour cart is currently empty, shop to add item!!")
            return
        print("\nName\tPrice\tQuantity")
        for product, quantity in self.cart.product_items.items():
            print(f"{product.name}\t{product.price}\t{quantity}")
        print(f"Total Price: {self.cart.total_price}")

    def pay_bill(self, shop):
        print(f"Total {self.cart.total_price} paid successfully")
        self.cart.clear()

    def __repr__(self) -> str:
        return f"<Customer {self.name} ({self.email})>"


# c1 = Customer("Kevin", "k@email.com", 4534324, "1234", "address")
# print(c1)
