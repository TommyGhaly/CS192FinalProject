from product import Product 

# Subclass of Product for Clothes category
class Clothes(Product):
    def __init__(self, product_id:str, name:str, price:float, description:str, stock_quantity:int, size:str, color:str, material:str):
        super().__init__(product_id, name, price, description, stock_quantity)
        self.size = size
        self.color = color
        self.material = material
        
    
    def get_details(self) -> str:
        return (f"Clothes[ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, "
                f"Size: {self.size}, Color: {self.color}, Material: {self.material}, "
                f"Stock: {self.stock_quantity}]")
        
    
    @staticmethod
    def to_dict(self) -> dict:
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
        
        
# completed