from typing import *
from .product import Product
from ..Inventory_Management.inventory import InventoryService
import json
import os
import logging

class ProductManagement():
    
    def __init__(self):
        self._products: List[Product] = ProductManagement.load_products()
        self.inventory = InventoryService()

    def add_product(self, product: Product):
        self._products.append(product)
        self.inventory.add_product(product.product_id, product.stock_quantity)
        InventoryService.save_inventory(self.inventory.inventory)
        ProductManagement.save_products(self._products)

    
    
    def remove_product(self, product_id:str, qty: int):
        new_prod = None
        for product in self._products:
            if product.product_id == product_id:
                new_prod= product
                break
        
        if new_prod.stock_quantity <= qty:
            new_prod.stock_quantity -= qty
            
            for i in range(self._products):
                if self._products[i].product_id == new_prod.product_id:
                    self._products[i] = new_prod
                    break
                    
            self.inventory.remove_product(product_id, qty)
            InventoryService.save_inventory(self.inventory.inventory)
            ProductManagement.save_products(self._products)
        else:
            logging.warning("Product not found.")
    
    
    def search_by_name(self, name:str) -> List[Product]:
        results = [] # list of products matching the name
        for product in self._products:
            if product.name.lower() == name.lower():
                results.append(product)
                
        return results
    
    
    def filter_by_price(self, min_price:float, max_price:float) -> List[Product]:
        results = list(filter(lambda p: min_price < p.price < max_price, self.inventory.inventory))
        return results
    
    
    def filter_by_category(self, category:str) -> List[Product]:
        results = [] # list of products matching the category
        for product in self._products:
            if isinstance(product, category):
                results.append(product) 
                
        return results
    
    def all_products(self) -> List[Product]:
        return self._products
    
    def get_price_by_id(self, product_id:str) -> float:
        for product in self._products:
            if product.product_id == product_id:
                return product.price
        return 0.0
    
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
    def load_products(filename: str = 'products.json') -> List[Product]:
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                return ProductManagement.from_dict(data)
        except FileNotFoundError:
            return []
    
    
    @staticmethod
    def save_products(products:List[Product]):
        with open('products.json', 'w') as f:
            json.dump(ProductManagement.to_dict(products), f, indent=4)
    
