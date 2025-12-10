from .product import Product
from typing import Dict

# Subclass of Product for Food category
class Food(Product):
    """
    Subclass that extends the Product 
    """
    def __init__(self, name:str, product_id: str, price:float, description:str, stock_quantity:int, expiration_date:str, is_organic:bool):
        """
        Initializatinon for the Food object.
        
        Args:
            name (str): The name of the Food.
            product_id (str): The product ID. 
            price (float): The price of the food.
            description (str): The description of the food
            stock_quantity (int): The number of the food in stock.
            expiration_date (str): The date of expiratiation for the food.
            is_organic (bool): Boolean to determine if food is organic
            
        Attributes:
            expiration_date: The expiration of the food.
            is_organic: Boolean to determine the organicness of the food.
        """
        
        super().__init__(product_id, name, price, description, stock_quantity)
        self.expiration_date = expiration_date # 'MM-DD-YYYY'
        self.is_organic = is_organic
        
    
    def get_details(self) -> str:
        """
        Overrided method to get a description of the food object.
        
        Returns:
            str: String containing all of the food's attributes
        """
        
        return (f"Food[ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, "
                f"Expiration Date: {self.expiration_date}, Organic: {self.is_organic}, "
                f"Stock: {self.stock_quantity}]")
        
    
    def to_dict(self) -> Dict:
        """
        Utility mehtod to convert the Food object into a dictionary
        
        Returns:
            dict: Dictionary containing all of the attributes of the Food object.
        """
        
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "stock_quantity": self.stock_quantity,
            "expiration_date": self.expiration_date,
            "is_organic": self.is_organic
        }