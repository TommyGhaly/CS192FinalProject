from .product import Product
from typing import Dict

# Subclass of Product for Electronics category
class Electronics(Product):
    """
    Subclass that extends the Product object    
    """
    
    def __inti__(self, name:str, product_id: str, price:float, description:str, stock_quantity: int, brand:str, model:str, warranty_period:int):
        """
        Initialization for the Electronics object.
        
        Args:
            name (str): The name of the electronic.
            product_id (str): The product ID.
            price (float): The price of the electronic.
            description (str): The describtion of the electronic.
            stock_quantity (int): The number of electronics in stock.
            brand (str): The brand of the electronic.
            model (str): The model of the electronic.
            warranty_period: The number of months that the warranty period lasts
            
        Attributes:
            brand: The brand of the electronic.
            model: The model of the electronic.
            warranty_period: The lenght of the warenty period in months
        """
        super().__init__(product_id, name, price, description, stock_quantity)
        self.brand = brand
        self.model = model
        self.warranty_period = warranty_period  # in months
        
        
    def get_details(self) -> str:
        """
        Overrided method to display a description of the electronics object.
        
        Returns:
            str: String listing out all of the attributes of the electronics
        """
        
        return (f"Electronics[ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, "
                f"Brand: {self.brand}, Model: {self.model}, Warranty: {self.warranty_period} months, "
                f"Stock: {self.stock_quantity}]")
        
    
    def to_dict(self) -> Dict:
        """
        Utility method to convert the Electronic object into a dictionary
        
        Returns:
            dict: A dictionary containing all of the contents of the electronic object. 
        """
        
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "stock_quantity": self.stock_quantity,
            "brand": self.brand,
            "model": self.model,
            "warranty_period": self.warranty_period
        }
        