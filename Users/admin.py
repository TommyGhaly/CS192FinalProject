from .user import User
from ..Inventory_Management.inventory import InventoryService
from ..Products.productManagement import ProductManagement
from ..Products.product import Product
from typing import *
import json
import os

class Admin(User):
    """
    Admin subclass of User with inventory and product management capabilities
    """
    
    def __init__(self, user_id: str, username: str, email: str, password: str):
        """
        Initialization of the Admin object
        
        Args:
            user_id (str): Unique identifier for the admin
            username (str): Username for authentication
            email (str): Email address of the admin
            password (str): Password for admin account
            
        Attributes:
            inventory: InventoryService instance for managing product inventory
            product_management: ProductManagement instance for managing products
        """
        
        super().__init__(user_id, username, email, password)
        self.inventory = InventoryService()
        self.product_management = ProductManagement()

    
    def remove_inventory(self, product_id: str, quantity: int):
        """
        Method to remove a quantity of a product from inventory
        
        Args:
            product_id (str): ID of product to remove from inventory
            quantity (int): Quantity of product to remove
        """
        
        self.product_management.remove_product(product_id, quantity)
            
    
    def add_inventory(self, product: Product):
        """
        Method to add a quantity of a product to inventory
        
        Args:
            product (Product): Product object to add to inventory
        """
        
        self.product_management.add_product(product)
    
    
    def view_inventory(self) -> List[Dict]:
        """
        Method to retrieve all inventory data
        
        Returns:
            List[Dict]: List of all inventory items as dictionaries
        """
        
        if os.path.exists('../Inventory_Management/inventory.json'):
                
            with open('../Inventory_Management/inventory.json', 'r') as f:
                inventory = json.load(f)    
            return inventory
        
        else:
            return []
        
        
    def view_users(self) -> List[Dict]:
        """
        Method to retrieve all registered users
        
        Returns:
            List[Dict]: List of all users as dictionaries
        """
        
        if os.path.exists('users_data.json'):
            with open('users_data.json', 'r') as f:
                users = json.load(f)
            return users
        
        else:
            return []
    
    
    def veiw_orders(self) -> List[Dict]:
        """
        Method to retrieve all orders in the system
        
        Returns:
            List[Dict]: List of all orders as dictionaries
        """
        
        if os.path.exists('../Shoping/orders_data.json'):
            with open('../Shoping/orders_data.json', 'r') as f:
                orders = json.load(f)
            return orders
        else:
            return []
        