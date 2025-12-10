from .payment import Payment
import logging

class BankTransferPayment(Payment):
    """
    Bank Transfer payment implementation
    """
    
    def __init__(self, amount: float, bank_account: str):
        """
        Initialization of the BankTransferPayment object
        
        Args:
            amount (float): Total amount to be paid
            bank_account (str): Bank account identifier for the transfer
            
        Attributes:
            bank_account: Account number for bank transfer
        """
        super().__init__(amount)
        self.bank_account = bank_account
    
    
    
    def process_payment(self, amount: float, payment_info: dict) -> bool:
        """
        Process payment via bank transfer
        
        Args:
            amount (float): Amount to be processed
            payment_info (dict): Dictionary containing required fields:
                - account_number (str): Recipient's account number
                - routing_number (str): Bank routing number
                - account_name (str): Account holder name
                
        Returns:
            bool: True if payment processed successfully, False if required fields are missing
        """
        
        required = ['account_number', 'routing_number', 'account_name']
        for field in required:
            if field not in payment_info:
                logging.warning(f'Missing required payment info field: {field}')
                return False
        logging.log(f'Processing payment of ${amount} via Bank Transfer from account {self.bank_account} 🏦')
        return True