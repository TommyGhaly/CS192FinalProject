# Base product class

class Product:
    """
    Base class that all other products inherit from
    """
    
    def __init__(self, product_id:str, name:str, price:float, description:str, stock_quantity:int):
        """
        Initialization of the product class
        
        Args:
            product_id (str): The product's ID.
            name (str): The product's name.
            price (float): The product's price.
            description (str): The description of the product.
            stock_quantity (int): The number of that product in stock.
            
        Attributes:
            product_id: The product's ID.
            name: The product's name.
            price: The product's price.
            description: The product's description
            stock_quantity: The product's quantity
        """
        
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description
        self.stock_quantity = stock_quantity
        
        
    
    def get_details(self) -> str:
        """
        Method to return the details of the Product object.
        Meant to be overrided in each subclass
        
        Returns:
            str: String containing the details of the product object
        """
        
        return (f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, "
                f"Description: {self.description}, Stock: {self.stock_quantity}]")
    
    def to_dict(self) -> dict:
        """
        Utility method to convert a Product object into a dictionary to save in a JSON file
        
        Returns:
            dict: Dictionary containing all of the Product's attributes
        """
        
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "stock_quantity": self.stock_quantity
        }
    
    @classmethod
    def from_dict(cls, data:dict) -> 'Product':
        """
        Class method to convert a dictionary into a Product object
        
        Args:
            data (dict): Dictionary containing all of the necessary attributes for a product object
        
        Returns:
            Product: Product with the attributes described in the dictionary 
        """
        
        return cls(
            product_id=data['product_id'],
            name=data['name'],
            price=data['price'],
            description=data['description'],
            stock_quantity=data['stock_quantity']
        )
