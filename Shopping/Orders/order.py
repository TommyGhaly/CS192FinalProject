from typing import *
class Order():
    """
    Order recipt class
    """
    
    def __init__(self, order_id:str, customer_id:str, items:Dict, total_price: float, status:str, payment_info: Dict):
        """
        Initialization of the Order class
        
        Args:
            order_id (str): Order ID
            customer_id (str): Customer's ID
            item (dict): Dictionary containing each product and their quantity in the order
            total_price (float): cost of each item in the items dictionary
            status (str): string to describe the nature of the order 
            payment_info (dict): dictionary describing the payemnt used 
        
        Attributes:
            order_id: order ID
            customer_id: customer's ID
            items: products mapped to quantity
            total_price: total cost of all items
            _status: nature of order
            _payment: info for payment 
        """
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items 
        self.total_price = total_price
        self._status = status
        self._payment = payment_info
    
    
    @property
    def payment(self) -> Dict:
        """
        Property method to retrieve the payment info
        
        Returns:
            dict: payment info
        """
        
        return self._payment
    
    
    def to_dict(self) -> Dict:
        """
        Method to convert Order object into a dictionary
        
        Returns:
            dict: order object saved as a dictionary
        """
        
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
        """
        Class method to convert a dictionary into an Order object
        
        Args:
            data (dict): dictionary describing order object
        
        Returns:
            Order: order described by inputted dictionary
        """
        
        return cls(
            order_id=data['order_id'],
            customer_id=data['customer_id'],
            items=data['items'],
            total_price=data['total_price'],
            status=data['status'],
        )