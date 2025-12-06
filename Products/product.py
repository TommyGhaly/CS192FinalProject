# Base product class

class Product:
    def __init__(self, product_id:str, name:str, price:float, description:str, stock_quantity:int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description
        self.stock_quantity = stock_quantity
        
        
    
    def get_details(self) -> str:
        return (f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, "
                f"Description: {self.description}, Stock: {self.stock_quantity}]")
    
    
# completed