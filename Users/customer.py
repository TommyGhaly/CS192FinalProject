from .user import User
from typing import *
from ..Shopping.Carts.cart import Cart
from ..Shopping.Orders.orderService import OrderService


# Subclass of User for Customer able to place orders
class Customer(User):
    def __init__(self, user_id:str, username:str, email:str, password:str):
        super().__init__(user_id, username, email, password)
        self.cart = Cart(user_id)
        self.os = OrderService()
        self.order_history = self.os.list_orders_for_customer(user_id)
    
    def add_to_cart(self, product_id:str, quantity:int):
        pass
    
    def remove_from_cart(self, product_id:str, quantity:int):
        pass

    def place_order(self, order_details:dict):
        pass

    def checkout(self):
        pass
    
    def view_orders(self) -> List[Dict]:
        return self.order_history

    def to_dict(self) -> Dict:
        return {
            'user_id': self.user_id, 
            'username': self.username, 
            'email': self.email,
            'password': self.password,
            'cart': self.cart.get_items(), 
            'order_history': self.order_history
        }