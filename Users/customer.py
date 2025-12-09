from .user import User
from typing import *


# Subclass of User for Customer able to place orders
class Customer(User):
    def __init__(self, user_id:str, username:str, email:str, password:str, cart_id:str, order_history:List[Dict] = []):
        super().__init__(user_id, username, email, password)
        self.cart_id = cart_id
        self.order_history = order_history
    
    def add_to_cart(self, product_id:str, quantity:int):
        pass
    
    def remove_from_cart(self, product_id:str, quantity:int):
        pass
# Complete when doen with order service
    def place_order(self, order_details:dict):
        pass

    def checkout(self):
        pass
    
    def view_orders(self) -> List[Dict]:
        return self.order_history