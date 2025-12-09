from .payment import Payment
import logging

class ApplePayPayment(Payment):
    def __init__(self, amount: float, device_account_number: str):
        super().__init__(amount)
        self.device_account_number = device_account_number
    
    # Implementing the abstract method for Apple Pay payment
    def process_payment(self, amount: float, payment_info: dict) -> bool:
        required = ['device_token', 'transaction_token']
        for field in required:
            if field not in payment_info:
                logging.warning(f'Missing required payment info field: {field}')
                return False
            
        logging.log(f'Processing payment of ${amount} via Apple Pay from device account {self.device_account_number} 🍎')
        return True