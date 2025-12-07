import os
from ..Shoping.Orders.orderService import Order
from typing import *
import json

class DataManagement():

    @staticmethod
    def save_order_data(order: Order):
        if os.path.exists('orders_data.json'):
            with open('orders_data.json', 'r') as f:
                orders_data = json.load(f)
                orders_data.append(order.to_dict())
        else:
            orders_data = [order.to_dict()] 
            with open('orders_data.json', 'w') as f:
                json.dump(orders_data, f)
                
