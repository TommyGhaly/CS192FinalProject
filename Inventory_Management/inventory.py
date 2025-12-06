import json
from typing import *

class InventoryService():
    def __init__(self):
        try: 
            with open('inventory.json', 'r') as f:
                self.inventory = json.load(f)
        except FileNotFoundError:
            self.inventory = {}

    def add_product(self, product_id:str, quantity:int):
        if product_id not in self.inventory:
            self.inventory[product_id] = quantity
        else:
            self.inventory[product_id] += quantity
        
        InventoryService.save_inventory(self.inventory)
        
    def remove_product(self, product_id:str, quantity:int):
        if product_id in self.inventory:
            if self.inventory[product_id] >= quantity:
                self.inventory[product_id] -= quantity
            else:
                raise ValueError("Not enough stock to remove the requested quantity.")
        else:
            raise ValueError("Product not found in inventory.")
    
        InventoryService.save_inventory(self.inventory)
        
    
    @staticmethod 
    def save_inventory(inventory:Dict[str, int]):
        with open('inventory.json', 'w') as f:
            json.dump(inventory, f)
            
    @staticmethod
    def check_stock(product_name:str ) -> int:
        try:
            with open('inventory.json', 'r') as f:
                inventory = json.load(f)
                return inventory.get(product_name, 0)
        except FileNotFoundError:
            return 0
        
# completed