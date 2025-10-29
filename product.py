class ProductItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Product:
    def __init__(self):
        self.products = []

    def add_products(self, product_item):
        self.products.append(product_item)

    def show_products(self):
        print("---Product List---")
        print("Name\tPrice\tQuantity")
        for product in self.products:
            print(f"{product.name}\t{product.quantity}\t{product.price}")
