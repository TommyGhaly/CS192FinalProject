from user import User
from typing import *
import json

# Subclass of User for Admin able to update inventory
class Admin(User):
    def __init__(self, user_id:str, username:str, email:str, password:str):
        super().__init__(user_id, username, email, password)

    
    def remove_inventory(self, item_id:str, quantity:int):
        with open('../Inventory_Management/inventory.json', 'r') as f:
            inventory = json.load(f)
            
    
    def add_inventory(self, item_id:str, quantity:int):
        pass
    
    
    def view_inventory(self) -> List[Dict]:
        with open('../Inventory_Management/inventory.json', 'r') as f:
            inventory = json.load(f)    
        return inventory
    
    def view_users(self):
        pass
    
    def veiw_orders(self):
        pass