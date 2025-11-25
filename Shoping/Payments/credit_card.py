from payment import Payment

class creditCardPayment(Payment):
    def __init__(self, amount: float):
        super().__init__(amount)
    
    # Implementing the abstract method for Credit Card payment
    def process_payment(self):
        return f'Processing payment of ${self.amount} via Credit Card ⭐'