from .payment import Payment
import logging

class BankTransferPayment(Payment):
    def __init__(self, amount: float, bank_account: str):
        super().__init__(amount)
        self.bank_account = bank_account
    
    # Implementing the abstract method for Bank Transfer payment
    def process_payment(self, amount: float, payment_info: dict) -> bool:
        required = ['account_number', 'routing_number', 'account_name']
        for field in required:
            if field not in payment_info:
                logging.warning(f'Missing required payment info field: {field}')
                return False
        logging.log(f'Processing payment of ${amount} via Bank Transfer from account {self.bank_account} 🏦')
        return True