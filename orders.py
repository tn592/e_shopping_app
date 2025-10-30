from product import Product


class Order:
    def __init__(self) -> None:
        self.product_items = {}
        product = Product()

    def add_product_item(self, product_item, quantity):
        for p in self.product_items.keys():
            if p.name == product_item.name:
                self.product_items[p] += quantity
                break
        else:
            self.product_items[product_item] = quantity

    @property
    def total_price(self):
        return sum(
            product_item.price * quantity
            for product_item, quantity in self.product_items.items()
        )

    def clear(self):
        self.product_items = {}
