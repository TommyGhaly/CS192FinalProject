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
    """
    Order Service object to facilitate orders
    """
    
    def __init__(self):
        """
        Initialization for order service object
        
        Attributes:
            order_data: dictionary of all orders loaded from JSON file
            pm: product managment object
            inventory_service: inventory service object
            dm: data management object
        """
        
        self.order_data = OrderService.load_orders()
        self.pm = ProductManagement()
        self.inventory_service = InventoryService()
        self.dm = DataManagement()
        
        
    def create_order(self, cart: Cart, payment: Payment, payment_info: dict, order_id: str) -> Order:
        """
        Method to create and process orders
        
        Args:
            cart (Cart): Cart object containing all of the items in the order
            payment (Payment): Payment object showing how payment went through
            payment_info (dict): all the contents of the payment 
            order_id (str): order's ID
        """
        
        reserved_stock = {}
        items = cart.get_items()
        total_price = cart.get_total(self.pm)
        customer_id = cart.customer_id
        
        for key, value in items.items():
            
            if self.inventory_service.check_stock(key) > value: # ensure enough stock
                
                reserved_stock[key] = value
                logging.log(f'Reserving {value} of {key} stock')
                
            else:
                
                logging.warning(f'Not enough stock to process order. Releasing reserved stock')
                order = Order(order_id, customer_id, items, total_price, 'failed', payment_info) # create order object that fails
                self.order_data[order_id] = order.to_dict()
                self.dm.save_order_data(self.order_data)
                OrderService.save_orders(self.order_data)
                return order
        
                                
        if payment.process_payment(total_price, payment_info): # ensure payment processes correctly
            self.update_stocks(reserved_stock)
            logging.log(f'Order paid successfully!')
            order = Order(order_id, customer_id, cart.get_items(), total_price, 'paid', payment_info)
            self.order_data[order_id] = order.to_dict
            self.dm.save_order_data(self.order_data)
            OrderService.save_orders(self.order_data)
            return order
        
        else:
            logging.warning(f'Failed to process payment!')
            order = Order(order_id, customer_id, items, total_price, 'failed', payment_info)
            self.order_data[order_id] = order.to_dict()
            self.dm.save_order_data(self.order_data)
            OrderService.save_orders(self.order_data)
            return order
        
        
    def update_stocks(self, reserved_stock: Dict[str:int]):
        """
        Update the inventory and product list 
        
        Args:
            reserved_stock (Dict[str:int]): dictionary mapping each product bought with a quantity to update
                                            files
        """
        
        for key, value in reserved_stock.items():
            self.pm.remove_product(key, value)
    
    
    def get_order(self, order_id: str) -> Order:
        """
        Retrieve order from the order id
        
        Args:
            order_id (str): order's identifier
        
        Returns:
            Order: Order correlating to order_id
        """
        
        return Order.from_dict(self.order_data[order_id])
    
    
    def list_orders_for_customer(self, customer_id: str) -> List[Dict]:
        """
        Get list of Orders done by a certain customer
        
        Args:
            customer_id (str): customer's ID
        
        Returns:
            List[Order]: list of each order in a dictionary
        """
        
        orders = []
        for _, value in self.order_data:
            if value.get('customer_id', '') == customer_id:
                orders.append(value)
        
        return orders
    
    
    @staticmethod
    def load_orders():
        """
        Static method to load the orders from the JSON file
        """
        
        try: 
            with open('orders.json', 'r') as f:
                orders_data = json.load(f)
                return orders_data
        except FileNotFoundError:
            return {}


    @staticmethod
    def save_orders(orders_data: Dict[str, Dict]):
        """
        Static method to save the orders to JSON file
        
        Args:
            order_data (dict[str, dict]): order data in the form of dictionaries        
        """
        
        with open('orders.json', 'w') as f:
            json.dump(orders_data, f)  