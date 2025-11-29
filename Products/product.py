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
        
    
    @property
    def product_id(self) -> str:
        return self._product_id
    
    @product_id.setter
    def product_id(self, value: str):
        self._product_id = value    
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value
        
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value: float):
        self._price = value
        
    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, value: str):  
        self._description = value
        
    @property
    def stock_quantity(self) -> int:
        return self._stock_quantity
    
    @stock_quantity.setter
    def stock_quantity(self, value: int):
        self._stock_quantity = value
        
        
    @staticmethod
    def to_dict(product) -> dict:
        return {
            "product_id": product.product_id,
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "stock_quantity": product.stock_quantity
        }