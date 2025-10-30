class ProductItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (${self.price}) - {self.quantity} left"


class Product:
    def __init__(self):
        self.products = []

    def add_products(self, product_item):
        self.products.append(product_item)

    def find_product(self, product_name):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                return product
        return None

    def remove_product(self, product_name):
        pr = self.find_product(product_name)
        if pr:
            self.products.remove(pr)
            print("Product Removed")
        else:
            print("Product Not Found")

    def show_products(self):
        print("\n---Product List---")
        print("\nName\tPrice\tQuantity")
        has_stock = False
        for product in self.products:
            if product.quantity > 0:
                has_stock = True
                print(product)
        if not has_stock:
            print("No products available right now!")
