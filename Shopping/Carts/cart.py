from Products.productManagement import ProductManagement
from typing import *


class Cart():
    """
    Cart Object meant for each Customer
    """
    
    def __init__(self, customer_id: str):
        """
        Initialization of the Cart object
        
        Args:
            customer_id (str): ID of the cart's owner
            
        Attributes:
            customer_id: Customer's ID
            _items: Dictionary saving all of the customer's items and their quantities 
        """
        self.customer_id = customer_id
        self._items = {}  # product_id -> quantity mapping):
    
    
    def add_item(self, product_id: str, quantity: int):
        """
        Add item to the dictionary of items
        
        Args:
            product_id (str): ID of product looking to add
            quantity (int): Number of product looking to add
        """
        
        if product_id in self._items:
            self._items[product_id] += quantity
        else:
            self._items[product_id] = quantity
            
            
    def remove_item(self, product_id: str, qty: int):
        """
        Remove some quantity of a product from the cart
        
        Args:
            product_id (str): ID of product 
            qty (int): Number of product to remove
        """
        if product_id in self._items:
            if self._items[product_id] > qty:
                self._items[product_id] -= qty
            elif self._items[product_id] == qty:
                del self._items[product_id]
            else:
                raise ValueError("Not enough quantity in cart to remove the requested amount.")
        else:
            raise ValueError("Product not found in cart.")
        
        
    def update_quantity(self, product_id: str, qty: int):
        """
        Manually update the quantity of a product in the cart
        
        Args:
            product_id (str): Product ID
            qty (int): Number that the product quantity will be set to 
        """
        
        if qty < 0:
            raise ValueError("Quantity cannot be negative.")
        self._items[product_id] = qty
    
    
    def clear(self):
        """
        Method to clear all of the items in the cart
        """
        
        self._items.clear()
        
    
    def get_items(self) -> dict:
        """
        Method to return all of the items in items
        
        Returns:
            dict: dictionary of all products mapped to quantity in the cart
        """
        
        return self._items.copy()


    def get_total(self,product_management:ProductManagement) -> float:
        """
        Utility function to find the total of the cart
        
        Returns:
            float: price of each item in the cart
        """
        
        total = 0.0
        for product_id, qty in self._items.items():
            price = product_management.get_price_by_id(product_id)
            total += price * qty
        return total