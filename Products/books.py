from .product import Product

# Subclass for book products
class Book(Product):
    """
    Subclass that extends the Product class
    """
    
    def __init__(self, name:str, price:float, description:str, stock_quantity:int, author:str, publisher:str, isbn:str, genre:str):
        super().__init__('book', name, price, description, stock_quantity)
        self.author = author
        self.publisher = publisher
        self.isbn = isbn
        self.genre = genre
        
    
    def get_details(self) -> str:
        return (f"Book[ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, "
                f"Author: {self.author}, Publisher: {self.publisher}, ISBN: {self.isbn}, "
                f"Genre: {self.genre}, Stock: {self.stock_quantity}]")
        
    
    @staticmethod
    def to_dict(self) -> dict:
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
        
        
    
# completed