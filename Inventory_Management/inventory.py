import json
from typing import *

class InventoryService():
    def __init__(self):
        self.inventory: Dict[str, int] = InventoryService.load_inventory()

    def add_product(self, product_id:str):
        if product_id not in self.inventory:
            self.inventory[product_id] = 1
        else:
            self.inventory[product_id] += 1 
        
        InventoryService.save_inventory(self.inventory)
        
    def remove_product(self, product_id:str):
        if product_id in self.inventory:
            if self.inventory[product_id] >= 1:
                self.inventory[product_id] -= 1
            else:
                raise ValueError("Not enough stock to remove the requested quantity.")
        else:
            raise ValueError("Product not found in inventory.")
    
        InventoryService.save_inventory(self.inventory)

    def check_stock(self, product_name:str ) -> int:
        try:
            with open('inventory.json', 'r') as f:
                inventory = json.load(f)
                return inventory.get(product_name, 0)
        except FileNotFoundError:
            return 0
    
    @staticmethod 
    def save_inventory(inventory:Dict[str, int]):
        with open('inventory.json', 'w') as f:
            json.dump(inventory, f)
            
    @staticmethod 
    def load_inventory() -> Dict[str, int]:
        try:
            with open('inventory.json', 'r') as f:
                inventory = json.load(f)
                return inventory
        except FileNotFoundError:
            return {}

# completed