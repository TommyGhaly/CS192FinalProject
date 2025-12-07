from typing import *
from ...Users.customer import Customer
from ...Products.product import Product
from ...Inventory_Management.inventory import InventoryService
import logging
import json

class CartService():
    def __init__(self):
        self.carts: Dict[str, Dict[str, int]] = {}
        
    def add_product(self, customer: Customer, product: Product, qty: int):
        
        customer_id = customer.user_id
        product_id = product.product_id
        if customer_id not in self.carts:
            self.carts[customer_id] = {
                'price': 0
            }
            
        if product_id in self.carts[customer_id]:
            self.carts[customer_id][product_id] += qty
            self.carts[customer_id]['price'] += product.price * qty 
        else:
            self.carts[customer_id][product_id] = qty
            self.carts[customer_id]['price'] += product.price * qty
    
    def remove_product(self, customer: Customer, product: Product, qty: int):
        customer_id = customer.user_id
        product_id = product.product_id
        
        if customer_id in self.carts and product_id in self.carts[customer_id]:
            if self.carts[customer_id][product_id] <= qty:
                self.carts[customer_id]['price'] -= product.price * self.carts[customer_id][product_id]
                del self.carts[customer_id][product_id]
            else:
                self.carts[customer_id][product_id] -= qty
                self.carts[customer_id]['price'] -= product.price * qty
        else:
            logging.warning(f"Product {product_id} not in cart for customer {customer_id}")
            
            
    def get_cart(self, customer: Customer) -> Dict[str, int]:
        customer_id = customer.user_id
        return self.carts.get(customer_id, {})
    
    
    def clear_cart(self, customer: Customer):
        customer_id = customer.user_id
        if customer_id in self.carts:
            del self.carts[customer_id]
            
            
    @staticmethod
    def save_carts(carts: Dict[str, Dict[str, int]], filename: str = 'carts_data.json'):
        with open(filename, 'w') as f:
            json.dump(carts, f)