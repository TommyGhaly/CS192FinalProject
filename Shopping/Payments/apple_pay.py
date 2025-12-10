from .payment import Payment
import logging

class ApplePayPayment(Payment):
    """
    Apple Pay payment implementation
    """
    
    def __init__(self, amount: float, device_account_number: str):
        """
        Initialization of the ApplePayPayment object
        
        Args:
            amount (float): Total amount to be paid
            device_account_number (str): Device account number for Apple Pay
            
        Attributes:
            device_account_number: Account number associated with the device
        """
        
        super().__init__(amount)
        self.device_account_number = device_account_number
    
    
    def process_payment(self, amount: float, payment_info: dict) -> bool:
        """
        Process payment using Apple Pay
        
        Args:
            amount (float): Amount to be processed
            payment_info (dict): Dictionary containing required fields:
                - device_token (str): Token for the device
                - transaction_token (str): Token for the transaction
                
        Returns:
            bool: True if payment processed successfully, False if required fields are missing
        """
        
        required = ['device_token', 'transaction_token']
        for field in required:
            if field not in payment_info:
                logging.warning(f'Missing required payment info field: {field}')
                return False
            
        logging.log(f'Processing payment of ${amount} via Apple Pay from device account {self.device_account_number} 🍎')
        return True