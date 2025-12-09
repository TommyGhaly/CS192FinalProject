from .payment import Payment
import logging

class PayPalPayment(Payment):
    def __init__(self, amount: float, email: str):
        super().__init__(amount)
        self.email = email
    
    # Implementing the abstract method for PayPal payment
    def process_payment(self, amount: float, payment_info: dict) -> bool:
        required = ['email', 'password']
        for field in required:
            if field not in payment_info:
                logging.warning(f'Missing required payment info field: {field}')
                return False
        logging.log(f'Processing payment of ${amount} via PayPal for account {self.email} ⭐')
        return True