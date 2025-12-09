from ...Products.productManagement import ProductManagement
from typing import *


class Cart():
    def __init__(self, customer_id: str):
        self.customer_id = customer_id
        self._items = {}  # product_id -> quantity mapping):
    
    
    def add_item(self, product_id: str, quantity: int):
        if product_id in self._items:
            self._items[product_id] += quantity
        else:
            self._items[product_id] = quantity
            
    def remove_item(self, product_id: str, quantity: int):
        if product_id in self._items:
            if self._items[product_id] > quantity:
                self._items[product_id] -= quantity
            elif self._items[product_id] == quantity:
                del self._items[product_id]
            else:
                raise ValueError("Not enough quantity in cart to remove the requested amount.")
        else:
            raise ValueError("Product not found in cart.")
        
    def update_quantity(self, product_id: str, qty: int):
        if qty < 0:
            raise ValueError("Quantity cannot be negative.")
        self._items[product_id] = qty
    
    
    def clear(self):
        self._items.clear()
        
    
    def get_items(self) -> dict:
        return self._items.copy()


    def get_total(self,product_management:ProductManagement) -> float:
        total = 0.0
        for product_id, qty in self._items.items():
            price = product_management.get_price_by_id(product_id)
            total += price * qty
        return total