from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, price:float):
        self.price = price
        
        
    # Concrete method to get receipts
    def get_recipt(self):
        return f"Recipt: Paid ${self.amount} using {type(self).__name__}."
    
    
    @abstractmethod
    def process_payment(self, amount: float, payment_info: dict) -> bool:
        raise NotImplementedError("Subclasses must implement this method")
        