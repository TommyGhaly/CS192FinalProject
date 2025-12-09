from .order import Order
from ..Carts.cart import Cart
from ..Payments.payment import Payment
from typing import *
import json 

class OrderService():
    def __init__(self):
        self.order_data = OrderService.load_orders()
    def create_order(self, cart: Cart, payment: Payment, payment_info: dict) -> Order:
        pass
    
    def get_order(self, order_id: str) -> Order:
        pass
    
    def list_orders_for_customer(self, customer_id: str) -> List[Order]:
        pass
    
    @staticmethod
    def load_orders():
        try: 
            with open('orders.json', 'r') as f:
                orders_data = json.load(f)
                return orders_data
        except FileNotFoundError:
            return {}

    @staticmethod
    def save_orders(orders_data: Dict[str, Dict]):
        with open('orders.json', 'w') as f:
            json.dump(orders_data, f)  