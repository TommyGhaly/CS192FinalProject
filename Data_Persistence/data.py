from typing import *
import json
import os

class DataManagement():
    """
    Data Service Class that will be called in other files to have one big JSON data
    file
    """
    def __init__(self):
        """
        Initialize the class by setting the data file path and loading its contents.

        This constructor assigns the path to the JSON data file and loads its
        contents using `DataManagement.load_data`.

        Attributes:
            filepath (str): Path to the JSON data file.
            data (dict): Data loaded from the JSON file
        """
        self.filepath = './Data_Persistence/data.json'
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
        
           
    @staticmethod
    def load_data(filename: str) -> Dict:
        """
        Static method to safely load the data from the JSON file located at the given filename.

        This method handles several edge cases to prevent JSON decoding errors:
            - If the file does not exist, it creates a new file with a default data structure.
            - If the file exists but is empty, it initializes it with a default data structure.
            - If the file exists but contains invalid/corrupted JSON, the file is reset to defaults.

        Args:
            filename (str): A string containing the location of the JSON file.

        Returns:
            dict: The loaded JSON data as a Python dictionary.
        """

        # If file doesn't exist → create it with a base structure
        if not os.path.exists(filename):
            default = DataManagement.default_data()
            DataManagement.save_data(default, filename)
            return default

        # If file exists but is empty → reset to defaults
        if os.path.getsize(filename) == 0:
            default = DataManagement.default_data()
            DataManagement.save_data(default, filename)
            return default

        # Normal load attempt
        try:
            with open(filename, 'r') as f:
                return json.load(f)

        except (json.JSONDecodeError, ValueError):
            # File is corrupted → restore default structure
            default = DataManagement.default_data()
            DataManagement.save_data(default, filename)
            return default


    @staticmethod
    def default_data() -> Dict:
        """
        Static method returning the base data structure for the entire E-Shop system.

        This ensures a consistent format for the JSON file, even if the file is newly created
        or corrupted.

        Returns:
            dict: A dictionary containing empty sections for products, orders, users,
                  inventory, and payments.
        """
        return {
            "products": {},
            "orders": {},
            "users": {},
            "inventory": {},
        }


    @staticmethod
    def save_data(data: Dict, filename: str):
        """
        Static method to save the complete data dictionary into the JSON file.

        This method guarantees that the data is cleanly written to the file and properly
        formatted using indentation.

        Args:
            data (dict): Complete dictionary of all system data.
            filename (str): The location of the JSON file to save to.
        """
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
