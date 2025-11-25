from user import User

# Subclass of User for Customer able to place orders
class Customer(User):
    def __init__(self, user_id:str, username:str, email:str, password:str):
        super().__init__(user_id, username, email, password)