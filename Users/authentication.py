from user import User
import json
from typing import *

class AuthenticationSystem():
    def __init__(self):
        try: 
            with open('users_data.json', 'r') as f:
                self.users_data = json.load(f)
        except FileNotFoundError:
            self.users_data = {}
    
    
    def register_user(self, user:User):
        if self.authenticate_user(user.username, user.password):
            
            self.users_data[user.username] = user.to_dict()
            with open('users_data.json', 'w') as f:
                json.dump(self.users_data, f)
        else:
            raise ValueError("User already exists")
    
    def authenticate_user(self, username:str, password:str) -> bool:
        
        for user in self.users_data.values():
            if user['username'] == username or user['password'] == password:
                return False
        return True
    
    
    def logout_user(self, user:User):
        pass
    
    
    def login_user(self, username:str, password:str) -> Optional[User]:
        pass