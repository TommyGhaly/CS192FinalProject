from .payment import Payment
import logging

class PayPalPayment(Payment):
    """
    PayPal payment implementation
    """
    
    def __init__(self, amount: float, email: str):
        """
        Initialization of the PayPalPayment object
        
        Args:
            amount (float): Total amount to be paid
            email (str): Email address associated with PayPal account
            
        Attributes:
            email: PayPal account email address
        """
        
        super().__init__(amount)
        self.email = email
    
    
    def process_payment(self, amount: float, payment_info: dict) -> bool:
        """
        Process payment via PayPal
        
        Args:
            amount (float): Amount to be processed
            payment_info (dict): Dictionary containing required fields:
                - email (str): PayPal account email
                - password (str): PayPal account password
                
        Returns:
            bool: True if payment processed successfully, False if required fields are missing
        """
        
        required = ['email', 'password']
        for field in required:
            if field not in payment_info:
                logging.warning(f'Missing required payment info field: {field}')
                return False
        logging.log(f'Processing payment of ${amount} via PayPal for account {self.email} ⭐')
        return True