import os
from ..Shopping.Orders.orderService import Order
from typing import *
import json

class DataManagement():

    def __init__(self):
        self.filepath = 'data.json'
        self.data = DataManagement.load_data(self.filepath)

    def save_order_data(self, order_data: Dict):
        if 'orders' not in self.data:
            self.data['orders'] = order_data
        else:
            self.data['orders'].update(order_data)
        
        DataManagement.save_data(self.data, self.filepath)

    def save_user_data(self, user_data: Dict):
        if 'users' not in self.data:
            self.data['users'] = user_data
        else:
            self.data['users'].update(user_data)
            
        DataManagement.save_data(self.data, self.filepath)

    def save_product_data(self, product_data: Dict):
        pass
    
    def save_inventory_data(self, inventory_data: Dict):
        pass
    
    def save_cart_data(self, cart_data: Dict):
        pass
    
    def save_payment_data(self, payment_data: Dict):
        pass
    
    @staticmethod
    def load_data(filename: str) -> Dict:
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            return {}
        
    @staticmethod
    def save_data(data: Dict, filename: str):
        with open(filename, 'w') as f:
            json.dump(data, f)