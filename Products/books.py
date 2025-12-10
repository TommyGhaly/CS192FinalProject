from .product import Product

# Subclass for book products
class Book(Product):
    """
    Subclass that extends the Product class
    """
    
    def __init__(self, name:str, price:float, description:str, stock_quantity:int, author:str, publisher:str, isbn:str, genre:str):
        """
        Initialize a Book object, inheriting from the Product class.

        Calls the parent `Product` constructor with the product type 'book' 
        and sets the book-specific attributes.

        Args:
            name (str): The name of the book.
            price (float): The price of the book.
            description (str): A short description of the book.
            stock_quantity (int): The number of copies available in stock.
            author (str): The author of the book.
            publisher (str): The publisher of the book.
            isbn (str): The ISBN identifier of the book.
            genre (str): The genre or category of the book.

        Attributes:
            author (str): The author of the book.
            publisher (str): The publisher of the book.
            isbn (str): The ISBN identifier of the book.
            genre (str): The genre or category of the book.
        """
        super().__init__('book', name, price, description, stock_quantity)
        self.author = author
        self.publisher = publisher
        self.isbn = isbn
        self.genre = genre
        
    
    def get_details(self) -> str:
        """
        Overrided `get_details` method that returns a string that includes all of the object's attributes
        
        Returns:
            str: String describing all of the properties of the Book object
        """
        
        return (f"Book ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, "
                f"Author: {self.author}, Publisher: {self.publisher}, ISBN: {self.isbn}, "
                f"Genre: {self.genre}, Stock: {self.stock_quantity}]")
        
    
    @staticmethod
    def to_dict(self) -> dict:
        """
        Static method to convert object into a dictionary
        
        Returns: 
            dict: dictionary contiaining all of the attributes of the Book object
        """
        
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "stock_quantity": self.stock_quantity,
            "author": self.author,
            "publisher": self.publisher,
            "isbn": self.isbn,
            "genre": self.genre
        }