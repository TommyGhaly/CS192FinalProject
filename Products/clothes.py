from .product import Product 

# Subclass of Product for Clothes category
class Clothes(Product):
    """
    Subclass that extends Product    
    """
    
    def __init__(self, name:str, product_id:str, price:float, description:str, stock_quantity: int, size:str, color:str, material:str):
        """
        Initialize a Cloth object, inheriting from the Product class.

        Calls the parent `Product` constructor with the product type 'cloth' 
        and sets the cloth-specific attributes.

        Args:
            name (str): The name of the clothing.
            product_id (str): The product ID
            price (float): The price of the clothing.
            description (str): A short description of the clothing.
            stock_quantity (int): The number of these clothes in stock
            size (str): The size of the piece of clothing (ex. "small", "medium", "large").
            color (str): Color of the clothing.
            material (str): Material of clothing. 

        Attributes:
            size (str): The size of clothing.
            color (str): The color of the clothing. 
            material (str): The material of the clothing.
        """
        super().__init__(product_id, name, price, description, stock_quantity)
        self.size = size
        self.color = color
        self.material = material
        
    
    def get_details(self) -> str:
        """
        Overrided method to retrieve the details of the cloth
        
        Returns:
            str: string describing all of the cloth's attributes
        """
        
        return (f"Cloth ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, "
                f"Size: {self.size}, Color: {self.color}, Material: {self.material}, "
                f"Stock: {self.stock_quantity}]")
        
    
    def to_dict(self) -> dict:
        """
        Method to convert the attributes of the clothing object into a dictonary
        
        Returns:
            dict: dictionary with all of the object's attributes
        """
        
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "stock_quantity": self.stock_quantity,
            "size": self.size,
            "color": self.color,
            "material": self.material
        }