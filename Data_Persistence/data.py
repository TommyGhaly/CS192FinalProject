"""
Data Service Class that will be called in other files to have one big JSON data
file
"""

from typing import *
import json

class DataManagement():

    def __init__(self):
        """
        Initialize the class by setting the data file path and loading its contents.

        This constructor assigns the path to the JSON data file and loads its
        contents using `DataManagement.load_data`.

        Attributes:
            filepath (str): Path to the JSON data file.
            data (dict): Data loaded from the JSON file
        """
        self.filepath = 'data.json'
        self.data = DataManagement.load_data(self.filepath)


    def save_order_data(self, order_data: Dict):
        """
        Save new order data into the main JSON data structure.

        Args:
            order_data (dict): A dictionary containing the order data to save.
        """
        
        if 'orders' not in self.data:
            self.data['orders'] = order_data
        else:
            self.data['orders'].update(order_data)
        
        DataManagement.save_data(self.data, self.filepath)


    def save_user_data(self, user_data: Dict):
        """
        Save new user data into the main JSON data structure

        Args:
            user_data (dict): A dictionary containing the user data to save.
        """
        
        if 'users' not in self.data:
            self.data['users'] = user_data
        else:
            self.data['users'].update(user_data)
            
        DataManagement.save_data(self.data, self.filepath)

    def save_product_data(self, product_data: Dict):
        """
        Save new product data into the main JSON data structure.

        Args:
            product_data (dict): A dictionary containing the product data to save.
        """
        
        if 'products' not in self.data:
            self.data['products'] = product_data
        
        else:
            self.data['products'].update(product_data)
            
        DataManagement.save_data(self.data, self.filepath)
           
           
    def save_inventory_data(self, inventory_data: Dict):
        """
        Save new inventory data into the main JSON data structure.

        Args:
            inventory_data (dict): A dictionary containing the inventory data to save.
        """
        
        if 'inventory' not in self.data:
            self.data['inventory'] = inventory_data
        else:
            self.data['inventory'].update(inventory_data)
        
        DataManagement.save_data(self.data, self.filepath)
    
    
    def save_cart_data(self, cart_data: Dict):
        """
        Save new cart data into the main JSON data structure.

        Args:
            cart_data (dict): A dictionary containing the cart data to save.
        """
        
        if 'carts' not in self.data:
            self.data['carts'] = cart_data
        else:
            self.data['carts'].update(cart_data)
        
        DataManagement.save_data(self.data, self.filepath)
        
    
    def save_payment_data(self, payment_data: Dict):
        """
        Save new payment data into the main JSON data structure.

        Args:
            payment_data (dict): A dictionary containing the payment data to save.
        """
        
        if 'payments' not in self.data:
            self.data['payments'] = payment_data
        else:
            self.data['payments'].update(payment_data)

        DataManagement.save_data(self.data, self.filepath) 
        
           
    @staticmethod
    def load_data(filename: str) -> Dict:
        """
        Static method to load the data from the JSON file locaed at the filename
        
        Args:
            filename (str): A string containing the location of the JSON file
        """
        
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            with open(filename, 'w') as f:
                f.write("")
            return {}
        
        
    @staticmethod
    def save_data(data: Dict, filename: str):
        """
        Static method to save the contents of the `self.data` attribute into the JSON file
        
        Args:
            data (dict): Complete dictonary of all the data from the entire E-Shop System
        """ 
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)