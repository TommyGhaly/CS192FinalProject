from typing import *
from .product import Product
from ..Inventory_Management.inventory import InventoryService
from ..Data_Persistence.data import DataManagement
import json
import logging

class ProductManagement():
    """
    Service object to Manage the products 
    """
    
    def __init__(self):
        """
        Initialization for the Product Service object
        
        Attributes:
            _products (List[Product]): a list of all the available products
            inventory (InventoryService): The inventory service object used to verify the correct inventory
            dm (DataManagement): the data management service
        """
        
        self._products: List[Product] = ProductManagement.load_products()
        self.inventory = InventoryService()
        self.dm = DataManagement()

    def add_product(self, product: Product):
        """
        Add a product to the list of products and the inventory 
        
        Args:
            product (Product): the product to be added
        """
        
        self._products.append(product)
        self.inventory.add_product(product.product_id, product.stock_quantity)
        InventoryService.save_inventory(self.inventory.inventory)
        self.save_products(self._products)

    
    
    def remove_product(self, product_id:str, qty: int):
        """
        Remove a product from the products list and the inventory
        
        Args:
            product_id (str): reference to product that will be removed
            qty (int): the quantity of the product that will be removed
        """
        
        new_prod = None
        for product in self._products:
            if product.product_id == product_id: # Identify which product object correlates to the product_id
                new_prod = product
                break
        
        if new_prod.stock_quantity <= qty:
            new_prod.stock_quantity -= qty
            
            for i in range(self._products):
                if self._products[i].product_id == new_prod.product_id:
                    self._products[i] = new_prod
                    break
                    
            self.inventory.remove_product(product_id, qty)
            InventoryService.save_inventory(self.inventory.inventory)
            self.save_products(self._products)
        else:
            logging.warning("Product not found.")
    
    
    def search_by_name(self, name:str) -> List[Dict]:
        """
        Method to search for products by name
        
        Args:
            name (str): name of the product searched for 
        
        Returns:
            List[Dict]: A complete list of the products that correlate to the correct name 
                        converted to dictionaries
        """
        
        results = [] # list of products matching the name
        for product in self._products:
            if product.name.lower() == name.lower():
                results.append(product.to_dict())
                
        return results
    
    
    def filter_by_price(self, min_price:float, max_price:float) -> List[Dict]:
        """
        Method to filter the products based off price
        
        Args:
            min_price (float): The minimum price to search for 
            max_price (float): The maximum price to search for 
            
        Returns:
            List[Dict]: A complete list of the products that are in the price rage converted 
                        to dictionaries
        """
        
        results = list(x.to_dict() for x in 
                       filter(lambda p: min_price < p.price < max_price,
                              self.inventory.inventory))
        return results
    
    
    def filter_by_category(self, category:str) -> List[Dict]:
        """
        Method to filter based on category
        
        Args:
            category (str): The category to search for
            
        Returns:
            List[Dict]: A complete list of the products in the categroy 
                        converted to dictionaries
        """
        
        results = [] # list of products matching the category
        for product in self._products:
            if isinstance(product, category):
                results.append(product) 
                
        return results
    
    def all_products(self) -> List[Dict]:
        """
        Method to return all of the products
        
        Returns:
            List[Dict]: A complete list of all the products as dictionaries
        """
        
        return [x.to_dict() for x in self._products]
    
    def get_price_by_id(self, product_id:str) -> float:
        """
        Method to retrieve a price of a product from the produce's ID
        
        Args:
            product_id (str): Product's ID
            
        Returns:
            float: The price in dollars 
        """
        
        for product in self._products:
            if product.product_id == product_id:
                return product.price
        return 0.0


    def save_products(self, products:List[Product]):
        with open('products.json', 'w') as f:
            json.dump(self.to_dict(products), f, indent=4)
        self.dm.save_product_data(self.to_dict(products))
    
    
    def to_dict(self, products: List[Product]) -> List[Dict]:
        """
        Method to convert products list into a list of dictionaries to store in memory
        
        Args:
            products (List[Product]): List of products
            
        Returns:
            List[Dict]: List of products converted to dictionaries
        """
        
        return [product.to_dict() for product in products]
    
    
    @staticmethod
    def from_dict(data:List[Dict]) -> List[Product]:
        """
        Utility function to convert a list of dictionaries into the list of products 
        
        Args:
            data (List[Dict]): the list of products in the form of a dictionary
        
        Returns:
            List[Product]: the product list 
        """
        
        products = []
        for item in data:
            product = Product(
                product_id=item['product_id'],
                name=item['name'],
                price=item['price'],
                description=item['description'],
                stock_quantity=item['stock_quantity']
            )
            products.append(product)
        return products
    
    
    @staticmethod
    def load_products(filename: str = 'products.json') -> List[Product]:
        """
        Static mehtod to load the products from the filepath
        
        Args:
            filename (str): name of file path
            
        Returns:
            List[Products]: List of products 
        """
        
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                return ProductManagement.from_dict(data)
        except FileNotFoundError:
            return []

    
