from ..Products.product import Product
from typing import *

class Order():
    def __init__(self, order_id: str, customer:str, items: List[Product], total_price: float, status: str):
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.total_price = total_price
        self.status = status  # e.g., "Pending", "Shipped", "Delivered" 