from typing import *
from ..Products.product import Product
from ..Inventory_Management.inventory import InventoryService
import json
import os
import logging

class ProductManagement():
    
    def __init__(self):
        try: 
            with open('products.json', 'r') as f:
                self.products_list = ProductManagement.from_dict(json.load(f))
        except FileNotFoundError:
            self.products_list = []   

        self.inventory = InventoryService()

    def add_product(self, product:Product, admin_id:str):
        if os.path.exists('../Users/user_data.py'):
            with open('../Users/user_data.py', 'r') as f:
                users_data = json.load(f)
                if users_data[admin_id]['is_admin']:
                    self.products_list.append(product)
                else:
                    logging.warning("Only admins can add products.")
        else:
            logging.warning("User data file not found.")
    
    
    def remove_product(self, product_id:str, admin_id:str):
        if os.path.exists('../Users/user_data.py'): # check if user data file exists
            with open('../Users/user_data.py', 'r') as f:
                users_data = json.load(f)
                if users_data[admin_id]['is_admin']: # check if user is admin
                    self.products_list = [prod for prod in self.products_list if prod.product_id != product_id]
                    self.inventory.remove_product(product_id, 0) # remove from inventory as well
                else:
                    logging.warning("Only admins can remove products.")
        else:
            logging.warning("User data file not found.")
    
    def search_by_name(self, name:str) -> List[Product]:
        results = [] # list of products matching the name
        for product in self.products_list:
            if product.name.lower() == name.lower():
                results.append(product)
                
        return results
    
    
    def filter_by_price(self, min_price:float, max_price:float) -> List[Product]:
        results = [] # list of products within the price range
        for product in self.products_list:
            if min_price <= product.price <= max_price:
                results.append(product)
                
        return results
    
    
    def filter_by_category(self, category:str) -> List[Product]:
        results = [] # list of products matching the category
        for product in self.products_list:
            if isinstance(product, category):
                results.append(product) 
                
        return results
    
    
    
    
    @staticmethod
    def from_dict(data:dict) -> List[Product]:
        products = []
        for item in data:
            product = Product(
                product_id=item['product_id'],
                name=item['name'],
                price=item['price'],
                description=item['description'],
                stock_quantity=item['stock_quantity']
            )
            products.append(product)
        return products
    
    
    
# completed