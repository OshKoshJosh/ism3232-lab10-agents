# stock_tool.py
# Author: Joshua Reddish


class StockLookup:
    """A tool that checks how many products are in stock."""

    def __init__(self, products):
        """Store the products and their quantities."""
        self.products = products

    def find_product(self, text):
        """Find a known product mentioned in a message."""
        for product in self.products:
            if product.lower() in text.lower():
                return product
        return None

    def count_for(self, product):
        """Return the quantity of a product."""
        return self.products.get(product)
