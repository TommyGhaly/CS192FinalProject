from ..Products.product import Product
from typing import *

class Order():
    def __init__(self, order_id: str, customer:str, items: List[Product], total_price: float, status: str):
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.total_price = total_price
        self.status = status  # e.g., "Pending", "Shipped", "Delivered" 
        
        
    def set_status(self, new_status: str):
        self.status = new_status
        
    def save_order(self):
        pass
    
    
    @staticmethod
    def to_dict(self) -> dict:
        return {
            "order_id": self.order_id,
            "customer": self.customer,
            "items": [item.to_dict() for item in self.items],
            "total_price": self.total_price,
            "status": self.status
        }