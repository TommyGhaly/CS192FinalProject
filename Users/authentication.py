from Users.user import User
import json
from typing import *
from Users.customer import Customer
from Users.admin import Admin
import logging

class AuthenticationService():
    """
    Service class for handling user authentication and registration
    """
    
    def __init__(self):
        """
        Initialization of the AuthenticationService object
        
        Attributes:
            users_data: Dictionary loaded from users_data.json containing all user information
        """
        
        try: 
            with open('users_data.json', 'r') as f:
                self.users_data = json.load(f)
        except FileNotFoundError:
            self.users_data = {}
    
    
    def register_user(self, user_id: str, username: str, email: str, password: str, is_admin: bool = False):
        """
        Method to register a new user in the system
        
        Args:
            user_id (str): Unique identifier for the new user
            username (str): Username for the new user
            email (str): Email address for the new user
            password (str): Password for the new user
            is_admin (bool): Flag to determine if user should be created as Admin or Customer (default: False)
        """
        
        if self.authenticate_user(username, password):
            
            if is_admin:
                new_user = Admin(user_id, username, email, password)
                self.users_data[user_id] = new_user.to_dict()
            else:
                new_user = Customer(user_id, username, email, password)
                self.users_data[user_id] = new_user.to_dict()
            
            AuthenticationService.save_users_data(self.users_data)
        else:
            logging.warning("Usernaem or password already exists.")
        
        
    
    def authenticate_user(self, username: str, password: str) -> bool:
        """
        Method to verify if username and password are available for new registration
        
        Args:
            username (str): Username to check
            password (str): Password to check
            
        Returns:
            bool: True if both username and password are available, False if either already exists
        """
        
        for user in self.users_data.values():
            if user['username'] == username or user['password'] == password:
                return False
        return True
    
    
    def logout_user(self, user: User):
        """
        Method to logout a user and update their login status
        
        Args:
            user (User): User object to logout
        """
        
        user.is_logged_in = False
        self.users_data[user.user_id]['is_logged_in'] = False
        AuthenticationService.save_users_data(self.users_data)
    
    
    def login_user(self, user: User, password: str) -> Optional[User]:
        """
        Method to login a user with password verification
        
        Args:
            user (User): User object attempting to login
            password (str): Password to verify against user's stored password
            
        Returns:
            Optional[User]: User object if login successful, None otherwise
        """
        
        if user.password == password:
            user.is_logged_in = True
            self.users_data[user.user_id]['is_logged_in'] = True
            AuthenticationService.save_users_data(self.users_data)

    
    
    @staticmethod
    def save_users_data(users_data: Dict[str, Dict]):
        """
        Static method to save users data to JSON file
        
        Args:
            users_data (Dict[str, Dict]): Dictionary of all users to save
        """
        
        with open('./Users/users_data.json', 'w') as f:
            json.dump(users_data, f)
            
    
    @staticmethod
    def load_users_data() -> Dict[str, Dict]:
        """
        Static method to load users data from JSON file
        
        Returns:
            Dict[str, Dict]: Dictionary of all users loaded from file, empty dict if file not found
        """
        
        try:
            with open('./Users/users_data.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}