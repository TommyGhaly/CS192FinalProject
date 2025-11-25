from typing import *
from ..Products.product import Product

class Cart():
    def __init__(self, items: List[Product] = None):
        if items is None:
            items = []
        self.items = items
        