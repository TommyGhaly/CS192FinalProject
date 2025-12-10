from .payment import Payment
import logging

class creditCardPayment(Payment):
    """
    Credit Card payment implementation
    """
    
    def __init__(self, amount: float):
        """
        Initialization of the creditCardPayment object
        
        Args:
            amount (float): Total amount to be paid
        """
        super().__init__(amount)
    
    
    def process_payment(self, amount: float, payment_info: dict) -> bool:
        """
        Process payment via credit card
        
        Args:
            amount (float): Amount to be processed
            payment_info (dict): Dictionary containing required fields:
                - card_number (str): Full credit card number
                - expiry_month (int): Card expiration month
                - expiry_year (int): Card expiration year
                - cvv (str): Card verification value
                - cardholder_name (str): Name on the card
                - billing_address (str): Billing address for the card
                
        Returns:
            bool: True if payment processed successfully, False if required fields are missing
        """
        
        required = ['card_number', 'expiry_month', 'expiry_year',  'cvv', 'cardholder_name', 'billing_address']
        for field in required:
            if field not in payment_info:
                logging.warning(f'Missing required payment info field: {field}')
                return False
        logging.log(f'Processing payment of ${amount} via Credit Card ending with {payment_info.get("card_number")[-4:]} 💳')
        return True