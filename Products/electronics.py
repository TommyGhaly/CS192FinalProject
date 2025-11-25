from product import Product

# Subclass of Product for Electronics category
class Electronics(Product):
    def __inti__(self, product_id:str, name:str, price:float, description:str, stock_quantity:int, brand:str, model:str, warranty_period:int):
        super().__init__(product_id, name, price, description, stock_quantity)
        self.brand = brand
        self.model = model
        self.warranty_period = warranty_period  # in months
        
        
    def get_details(self) -> str:
        return (f"Electronics[ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, "
                f"Brand: {self.brand}, Model: {self.model}, Warranty: {self.warranty_period} months, "
                f"Stock: {self.stock_quantity}]")