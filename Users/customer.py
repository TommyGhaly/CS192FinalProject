from .user import User
from typing import *
from Shopping.Carts.cart import Cart
from Shopping.Orders.orderService import OrderService
from Shopping.Payments.payment import Payment
import logging

class Customer(User):
    """
    Customer subclass of User with shopping and order functionality
    """
    
    def __init__(self, user_id: str, username: str, email: str, password: str):
        """
        Initialization of the Customer object
        
        Args:
            user_id (str): Unique identifier for the customer
            username (str): Username for authentication
            email (str): Email address of the customer
            password (str): Password for customer account
            
        Attributes:
            cart: Shopping cart associated with the customer
            os: OrderService instance for managing orders
            order_history: List of all orders placed by the customer
        """
        
        super().__init__(user_id, username, email, password)
        self.cart = Cart(user_id)
        self.os = OrderService()
        self.order_history = self.os.list_orders_for_customer(user_id)
    
    
    def add_to_cart(self, product_id: str, quantity: int):
        """
        Method to add an item to the customer's cart
        
        Args:
            product_id (str): ID of product to add
            quantity (int): Quantity of product to add
        """
        
        self.cart.add_item(product_id, quantity)
    
    
    def remove_from_cart(self, product_id: str, quantity: int):
        """
        Method to remove an item from the customer's cart
        
        Args:
            product_id (str): ID of product to remove
            quantity (int): Quantity of product to remove
        """
        
        self.cart.remove_item(product_id, quantity)

    
    def place_order(self, order_details: dict, payment: Payment):
        """
        Method to place an order with payment information
        
        Args:
            order_details (dict): Dictionary containing order details including payment_info and order_id
            payment (Payment): Payment object specifying payment method
        """
        
        order = self.os.create_order(self.cart, payment, 
                                order_details.get('payment_info', ''), 
                                order_details.get('order_id', ''))
        if order._status == 'paid':
            self.order_history.append(order.to_dict())
            self.checkout()
        else:
            self.order_history.append(order.to_dict())
            logging.warning(f'Failed to complete order! Please fix order inputs and try again.')


    def checkout(self):
        """
        Method to clear the cart after successful order placement
        """
        
        self.cart.clear()
    
    
    def view_orders(self) -> List[Dict]:
        """
        Method to retrieve all orders placed by the customer
        
        Returns:
            List[Dict]: List of all orders as dictionaries
        """
        
        return self.order_history

    
    def to_dict(self) -> Dict:
        """
        Method to convert Customer object to dictionary representation
        
        Returns:
            Dict: Customer object as dictionary with all attributes
        """
        
        return {
            'user_id': self.user_id, 
            'username': self.username, 
            'email': self.email,
            'password': self.password,
            'cart': self.cart.get_items(), 
            'order_history': self.order_history
        }