import os
from ..Shopping.Orders.orderService import Order
from typing import *
import json

class DataManagement():

    def __init__(self):
        try:
            with open('data.json', 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}

    def save_order_data(self, order: Order):
        pass

    def save_user_data(self, user_data: dict):
        pass

    def save_product_data(self, product_data: dict):
        pass
    
    def save_inventory_data(self, inventory_data: dict):
        pass
    
    def save_cart_data(self, cart_data: dict):
        pass
    
    def save_payment_data(self, payment_data: dict):
        pass
    
    