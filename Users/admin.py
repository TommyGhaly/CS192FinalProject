from user import User

# Subclass of User for Admin able to update inventory
class Admin(User):
    def __init__(self, user_id:str, username:str, email:str, password:str):
        super().__init__(user_id, username, email, password)

    
    def update_inventory(self, item_id:str, quantity:int):
        pass