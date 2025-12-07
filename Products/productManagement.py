from typing import *
from .product import Product
from ..Inventory_Management.inventory import InventoryService
from ..Users.admin import Admin
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

    def add_product(self, product:Product, admin:Admin):
        if isinstance(admin, Admin):
            self.products_list.append(product)
            self.inventory.add_product(product.product_id)
            InventoryService.save_inventory(self.inventory.inventory)
            ProductManagement.save_products(self.products_list)
        else:
            logging.warning("Only admins can add products.")
    
    
    def remove_product(self, product_id:str, admin:Admin):
        if isinstance(admin, Admin):
            product_to_remove = None
            for product in self.products_list:
                if product.product_id == product_id:
                    product_to_remove = product
                    break
            
            if product_to_remove:
                self.products_list.remove(product_to_remove)
                self.inventory.remove_product(product_id)
                InventoryService.save_inventory(self.inventory.inventory)
                ProductManagement.save_products(self.products_list)
            else:
                logging.warning("Product not found.")
        else:
            logging.warning("Only admins can remove products.")
    
    def search_by_name(self, name:str) -> List[Product]:
        results = [] # list of products matching the name
        for product in self.products_list:
            if product.name.lower() == name.lower():
                results.append(product)
                
        return results
    
    
    def filter_by_price(self, min_price:float, max_price:float) -> List[Product]:
        results = list(filter(lambda p: min_price < p.price < max_price, self.inventory.inventory))
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
    
    @staticmethod
    def to_dict(products:List[Product]) -> List[dict]:
        return [product.to_dict() for product in products]
    
    
    @staticmethod
    def save_products(products:List[Product]):
        with open('products.json', 'w') as f:
            json.dump(ProductManagement.to_dict(products), f, indent=4)
    
# completed