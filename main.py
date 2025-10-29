from users import Customer, Seller
from product import ProductItem
from shop import Shop


# def customer_query():
#     name = input("Enter your name:")
#     email = input("Enter your email: ")
#     phone = input(int("Enter your phone: "))
#     password = input(int("Enter Password: "))
#     address = input("Enter your address: ")
#     customer = Customer(
#         name=name, email=email, phone=phone, password=password, address=address
#     )

#     while True:
#         print(f"Welcome {customer.name}")
#         print("1. View all products")
#         print("2. Add product to cart")
#         print("3. View Cart")
#         print("4. Pay Bill")
#         print("5. Exit")


p1 = ProductItem("Laptop", 4, 45.90)
p2 = ProductItem("Mobile", 3, 23.20)
s1 = Seller("John", "j@example.com", 4332423, "1234", "addr")
shop = Shop("techshop")
s1.add_products(shop, p1)
s1.add_products(shop, p2)
shop.product.show_products()
