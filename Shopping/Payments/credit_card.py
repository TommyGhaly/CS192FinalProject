from .payment import Payment
import logging

class creditCardPayment(Payment):
    def __init__(self, amount: float):
        super().__init__(amount)
    
    # Implementing the abstract method for Credit Card payment
    def process_payment(self, amount: float, payment_info: dict) -> bool:
        required = ['card_number', 'expiry_month', 'expiry_year',  'cvv', 'cardholder_name', 'billing_address']
        for field in required:
            if field not in payment_info:
                logging.warning(f'Missing required payment info field: {field}')
                return False
        logging.log(f'Processing payment of ${amount} via Credit Card ending with {payment_info.get("card_number")[-4:]} 💳')
        return True