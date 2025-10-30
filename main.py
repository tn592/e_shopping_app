from users import Customer, Seller
from product import ProductItem
from shop import Shop

sh = Shop("TechShop")


def seller_query():
    name = input("\nEnter your name: ")
    email = input("Enter your email: ")
    phone = int(input("Enter your phone: "))
    password = input("Enter Password: ")
    address = input("Enter your address: ")
    seller = Seller(
        name=name, email=email, phone=phone, password=password, address=address
    )

    while True:
        print(f"\nWelcome {seller.name}")
        print("------------------")
        print("1. View all products")
        print("2. Add product")
        print("3. Remove product")
        print("4. Exit")

        choice = int(input("\nEnter Your Choice: "))

        if choice == 1:
            seller.show_products(sh)
        elif choice == 2:
            name = input("Enter Product Name: ")
            price = int(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = ProductItem(name=name, price=price, quantity=quantity)

            seller.add_products(sh, product)
        elif choice == 3:
            product = input("Enter product name to remove: ")
            seller.remove_product(sh, product)
        elif choice == 4:
            break
        else:
            print("Invalid Choice")


def customer_query():
    name = input("\nEnter your name: ")
    email = input("Enter your email: ")
    phone = int(input("Enter your phone: "))
    password = input("Enter Password: ")
    address = input("Enter your address: ")
    customer = Customer(
        name=name, email=email, phone=phone, password=password, address=address
    )

    while True:
        print(f"\nWelcome {customer.name}")
        print("------------------")
        print("1. View all products")
        print("2. Add product to cart")
        print("3. Remove product from cart")
        print("4. View Cart")
        print("5. Pay Bill")
        print("6. Exit")

        choice = int(input("\nEnter Your Choice: "))

        if choice == 1:
            customer.view_all_products(sh)
        elif choice == 2:
            product_name = input("Enter Product Name: ")
            quantity = int(input("Enter Quantity: "))
            customer.add_product_to_cart(sh, product_name, quantity)
        elif choice == 3:
            product_name = input("Enter product name to remove: ")
            quantity = int(input("Enter quantity: "))
            customer.remove_product_from_cart(sh, product_name, quantity)
        elif choice == 4:
            customer.view_cart()
        elif choice == 5:
            customer.pay_bill(sh)
        elif choice == 6:
            break
        else:
            print("Invalid Choice")


while True:
    print("\nWelcome to E Shopping App!")
    print("\n1. Seller")
    print("2. Customer")
    print("3. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        seller_query()
    elif choice == 2:
        customer_query()
    elif choice == 3:
        break
    else:
        print("Invalid Choice")
