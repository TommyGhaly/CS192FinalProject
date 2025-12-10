from abc import ABC, abstractmethod

class Payment(ABC):
    """
    Abstract base class for all payment methods
    """
    
    def __init__(self, price: float):
        """
        Initialization of the Payment object
        
        Args:
            price (float): Total amount to be paid
            
        Attributes:
            price: Amount for payment transaction
        """
        self.price = price
        
        
    def get_recipt(self) -> str:
        """
        Concrete method to generate payment receipt
        
        Returns:
            str: Receipt message with payment amount and method used
        """
        return f"Recipt: Paid ${self.amount} using {type(self).__name__}."
    
    
    @abstractmethod
    def process_payment(self, amount: float, payment_info: dict) -> bool:
        """
        Abstract method to process payment transaction
        
        Args:
            amount (float): Amount to be processed
            payment_info (dict): Dictionary containing payment details specific to payment method
            
        Returns:
            bool: True if payment processed successfully, False otherwise
        """
        
        raise NotImplementedError("Subclasses must implement this method")
        