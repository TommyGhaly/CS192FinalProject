import json
from typing import *
from Data_Persistence.data import DataManagement
class InventoryService():
    """
    Service class that tracks the inventory of each product and saves it to the inventory
    JSON file
    """
    
    def __init__(self):
        """
        Initialization of the Inventory Service object.
        Loads the inventory data using the `InventoryService.load_invnetory()`
        static method. Initializes the DataMangment object to store the inventory data 
        in a JSON file
        
        Attributes:
            self.inventory (dict): Dictonary containing all of the product's stocks
            self.data_service (DataManagement): DataManagement object used to store the inventory data
        """
        
        self.inventory: Dict[str, int] = InventoryService.load_inventory()
        self.data_service = DataManagement()

    def add_product(self, product_id:str, qty: int):
        """
        Method to add 1 level of stock to the inventory. First checks to see
        if the stock is present in `self.inventory` and then appends the ineger value
        by 1. Calls `InventoryService.save_inventory()` to update the JSON file containing
        all of the Inventory data in this file. Calls `self.data_service.save_inventory_data()`
        to save the Inventory data in the data JSON file.
        
        Args:
            product_id (str): Identification string to locate the stock that is to be updated
            qty (int): The number of a certain product to be added
        """
        
        if product_id not in self.inventory:
            self.inventory[product_id] = qty
        else:
            self.inventory[product_id] += qty
        
        InventoryService.save_inventory(self.inventory)
        self.data_service.save_inventory_data(self.inventory)
        
        
    def remove_product(self, product_id:str, qty: int):
        """
        Method to remove 1 unit of stock. Checks to see if there is adiquate level of stock before 
        removal. Saves updated inventory in both JSON files.
        
        Args:
            product_id (str): Identification string to locate the stock that is to be updated
            qty (int): The number of of a certain product to be removed
        """
        
        if product_id in self.inventory:
            if self.inventory[product_id] >= qty:
                self.inventory[product_id] -= qty
            else:
                raise ValueError("Not enough stock to remove the requested quantity.")
        else:
            raise ValueError("Product not found in inventory.")
    
        InventoryService.save_inventory(self.inventory)


    def check_stock(self, product_id:str ) -> int:
        """
        Utility function to check the level of stock remaining for a specific product
        
        Args:
            product_id (str): Identification string to locate the stock that is to be updated
            
        Returns:
            int: number coorelating to the stock of the product. Returns 0 if file is not found
        
        """
        
        try:
            with open('inventory.json', 'r') as f:
                inventory = json.load(f)
                return inventory.get(product_id, 0)
        except FileNotFoundError:
            return 0
    
    @staticmethod 
    def save_inventory(inventory:Dict[str, int]):
        """
        Static method to save the inventory dictionary into the JSON file
        
        Args:
            inventory (dict): Dictionary containing all of the contents of the Inventory
        """
        
        with open('./Inventory_management/inventory.json', 'w') as f:
            json.dump(inventory, f, indent=4)
            
    @staticmethod 
    def load_inventory() -> Dict[str, int]:
        """
        Static method to load the inventory from the JSON file
        
        Returns:
            Dict[str, int]: Dictionary data containing all of the inventory data. 
        """
        try:
            with open('./Inventory_management/inventory.json', 'r') as f:
                inventory = json.load(f)
                return inventory
        except FileNotFoundError:
            return {}
