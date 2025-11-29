import json
from typing import *
from ..Products.product import Product
class InventoryService():
    def __init__(self):
        try: 
            with open('inventory.json', 'r') as f:
                self.inventory = json.load(f)
        except FileNotFoundError:
            self.inventory = {}

    def add_product(self, product:Product, quantity:int):
        if product.__class__.__name__ not in self.inventory:
            self.inventory[product.__class__.__name__] = quantity
        else:
            self.inventory[product.__class__.__name__] += quantity
        
        InventoryService.save_inventory(self.inventory)
        
    def remove_product(self, product:Product, quantity:int):
        if product.__class__.__name__ in self.inventory:
            if self.inventory[product.__class__.__name__] >= quantity:
                self.inventory[product.__class__.__name__] -= quantity
            else:
                raise ValueError("Not enough stock to remove the requested quantity.")
        else:
            raise ValueError("Product not found in inventory.")
    
        InventoryService.save_inventory(self.inventory)
        
    
    @staticmethod 
    def save_inventory(inventory:Dict[str, int]):
        with open('inventory.json', 'w') as f:
            json.dump(inventory, f)