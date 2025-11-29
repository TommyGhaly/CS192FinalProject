from typing import *
from ..Products.product import Product
import json

class ProductManagement():
    
    def __init__(self):
        try: 
            with open('../Inventory_Management/inventory.json', 'r') as f:
                self.products_list = ProductManagement.from_dict(json.load(f))
        except FileNotFoundError:
            self.products_list = []     

    
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
            if product.__class__.__name__.lower() == category.lower():
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