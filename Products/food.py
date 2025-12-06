from product import Product

# Subclass of Product for Food category
class Food(Product):
    def __init__(self, product_id:str, name:str, price:float, description:str, stock_quantity:int, expiration_date:str, is_organic:bool):
        super().__init__(product_id, name, price, description, stock_quantity)
        self.expiration_date = expiration_date
        self.is_organic = is_organic
        
    
    def get_details(self) -> str:
        return (f"Food[ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, "
                f"Expiration Date: {self.expiration_date}, Organic: {self.is_organic}, "
                f"Stock: {self.stock_quantity}]")
        
    
    @staticmethod
    def to_dict(self) -> dict:
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "stock_quantity": self.stock_quantity,
            "expiration_date": self.expiration_date,
            "is_organic": self.is_organic
        }
        
        
# completed