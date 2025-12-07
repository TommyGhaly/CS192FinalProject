from .user import User
from ..Inventory_Management.inventory import InventoryService
from ..Products.productManagement import ProductManagement
from ..Products.product import Product
from typing import *
import json
import os

# Subclass of User for Admin able to update inventory
class Admin(User):
    def __init__(self, user_id:str, username:str, email:str, password:str):
        super().__init__(user_id, username, email, password)
        self.inventory = InventoryService()
        self.product_management = ProductManagement()

    
    def remove_inventory(self, product_id:str, quantity:int):
        for i in range(quantity):
            self.inventory.remove_product(product_id)
            self.product_management.remove_product(product_id, self)
            
    
    def add_inventory(self, product:Product, quantity:int):
        for i in range(quantity):
            self.inventory.add_product(product.product_id)
            self.product_management.add_product(product, self)
    
    
    def view_inventory(self) -> List[Dict]:
        if os.path.exists('../Inventory_Management/inventory.json'):
                
            with open('../Inventory_Management/inventory.json', 'r') as f:
                inventory = json.load(f)    
            return inventory
        
        else:
            return []
        
        
    def view_users(self):
        
        if os.path.exists('users_data.json'):
            with open('users_data.json', 'r') as f:
                users = json.load(f)
            return users
        
        else:
            return []
    
    def veiw_orders(self):
    
        if os.path.exists('../Shoping/orders_data.json'):
            with open('../Shoping/orders_data.json', 'r') as f:
                orders = json.load(f)
            return orders
        else:
            return []
        