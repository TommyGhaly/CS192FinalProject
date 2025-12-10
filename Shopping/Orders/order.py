from typing import *
class Order():
    def __init__(self, order_id:str, customer_id:str, items:Dict, total_price: float, status:str, payment_info: Dict):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items 
        self.total_price = total_price
        self._status = status
        self._payment = payment_info
    
    @property
    def payment(self) -> Dict:
        return self._payment
    
    def to_dict(self) -> Dict:
        return {
            'order_id': self.order_id,
            'customer_id': self.customer_id,
            'items': self.items,
            'total_price': self.total_price,
            'status': self._status,
            'payment': self._payment
        } 
    
    @classmethod
    def from_dict(cls, data:dict) -> 'Order':
        return cls(
            order_id=data['order_id'],
            customer_id=data['customer_id'],
            items=data['items'],
            total_price=data['total_price'],
            status=data['status'],
        )