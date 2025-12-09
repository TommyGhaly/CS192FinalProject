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
    
    @staticmethod
    def to_dict(self) -> dict:
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "stock_quantity": self.stock_quantity
        }
    
    @classmethod
    def from_dict(cls, data:dict) -> 'Product':
        return cls(
            product_id=data['product_id'],
            name=data['name'],
            price=data['price'],
            description=data['description'],
            stock_quantity=data['stock_quantity']
        )
    
# completed