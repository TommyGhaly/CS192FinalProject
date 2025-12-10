from .order import Order
from ..Carts.cart import Cart
from ..Payments.payment import Payment
from ...Products.productManagement import ProductManagement
from ...Inventory_Management.inventory import InventoryService
from ...Data_Persistence.data import DataManagement
from typing import *
import json 
import logging

class OrderService():
    def __init__(self):
        self.order_data = OrderService.load_orders()
        self.pm = ProductManagement()
        self.inventory_service = InventoryService()
        self.dm = DataManagement()
        
    def create_order(self, cart: Cart, payment: Payment, payment_info: dict, order_id: str) -> Order:
        reserved_stock = {}
        items = cart.get_items()
        total_price = cart.get_total(self.pm)
        customer_id = cart.customer_id
        
        for key, value in items.items():
            
            if self.inventory_service.check_stock(key) > value:
                
                reserved_stock[key] = value
                logging.log(f'Reserving {value} of {key} stock')
            else:
                
                logging.warning(f'Not enough stock to process order. Releasing reserved stock')
                order = Order(order_id, customer_id, items, total_price, 'failed', payment_info)
                self.order_data[order_id] = order.to_dict()
                self.dm.save_order_data(self.order_data)
                return order
        
                                
        if payment.process_payment(total_price, payment_info):
            self.update_stocks(reserved_stock)
            logging.log(f'Order paid successfully!')
            order = Order(order_id, customer_id, cart.get_items(), total_price, 'paid', payment_info)
            self.order_data[order_id] = order.to_dict
            self.dm.save_order_data(self.order_data)
            return order
        
        else:
            logging.warning(f'Failed to process payment!')
            order = Order(order_id, customer_id, items, total_price, 'failed', payment_info)
            self.order_data[order_id] = order.to_dict()
            self.dm.save_order_data(self.order_data)
            return order
        
        
    def update_stocks(self, reserved_stock: Dict[str:int]):
        for key, value in reserved_stock.items():
            for i in range(value):
                self.pm.remove_product(key)
    
    
    def get_order(self, order_id: str) -> Order:
        return Order.from_dict(self.order_data[order_id])
    
    def list_orders_for_customer(self, customer_id: str) -> List[Order]:
        orders = []
        for _, value in self.order_data:
            if value.get('customer_id', '') == customer_id:
                orders.append(Order.from_dict(value))
        
        return orders
    
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