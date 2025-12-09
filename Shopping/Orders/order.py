from typing import *
class Order():
    def __init__(self, order_id:str, customer_id:str, items:List[Dict], total_price: float, status:str, created_at:str):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items # List of dicts with product_id and quantity
        self.total_price = total_price
        self._status = status
        self.created_at = created_at

    
    def to_dict(self) -> dict:
        return {
            "order_id": self.order_id,
            "customer_id": self.customer_id,
            "items": self.items,
            "total_price": self.total_price,
            "status": self._status,
            "created_at": self.created_at
        } 
    
    @classmethod
    def from_dict(cls, data:dict) -> 'Order':
        return cls(
            order_id=data['order_id'],
            customer_id=data['customer_id'],
            items=data['items'],
            total_price=data['total_price'],
            status=data['status'],
            created_at=data['created_at']
        )