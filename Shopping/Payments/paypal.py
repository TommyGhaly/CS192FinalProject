from .payment import Payment

class PayPalPayment(Payment):
    def __init__(self, amount: float, email: str):
        super().__init__(amount)
        self.email = email
    
    # Implementing the abstract method for PayPal payment
    def process_payment(self):
        return f'Processing payment of ${self.amount} via PayPal (email: {self.email})'