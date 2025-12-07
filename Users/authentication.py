from .user import User
import json
from typing import *
from .customer import Customer
from .admin import Admin
import logging

class AuthenticationSystem():
    def __init__(self):
        try: 
            with open('users_data.json', 'r') as f:
                self.users_data = json.load(f)
        except FileNotFoundError:
            self.users_data = {}
    
    
    def register_user(self, user_id:str, username:str, email:str, password:str, is_admin:bool = False):
        if self.authenticate_user(username, password):
            
            if is_admin:
                new_user = Admin(user_id, username, email, password)
                self.users_data[user_id] = new_user.to_dict()
            else:
                new_user = Customer(user_id, username, email, password)
                self.users_data[user_id] = new_user.to_dict()
            
            AuthenticationSystem.save_users_data(self.users_data)
        else:
            logging.warning("Usernaem or password already exists.")
        
        
    
    def authenticate_user(self, username:str, password:str) -> bool:
        
        for user in self.users_data.values():
            if user['username'] == username or user['password'] == password:
                return False
        return True
    
    
    def logout_user(self, user:User):
        user.is_logged_in = False
        self.users_data[user.user_id]['is_logged_in'] = False
        AuthenticationSystem.save_users_data(self.users_data)
    
    
    def login_user(self, user:User, password:str) -> Optional[User]:
        if user.password == password:
            user.is_logged_in = True
            self.users_data[user.user_id]['is_logged_in'] = True
            AuthenticationSystem.save_users_data(self.users_data)

    
    
    @staticmethod
    def save_users_data(users_data:Dict[str, Dict]):
        with open('users_data.json', 'w') as f:
            json.dump(users_data, f)
            
    
    @staticmethod
    def load_users_data() -> Dict[str, Dict]:
        try:
            with open('users_data.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        
        
# completed