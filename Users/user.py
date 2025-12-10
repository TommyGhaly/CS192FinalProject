from typing import Dict

class User:
    """
    Main User class that serves as the base for all user types in the system
    """
    
    def __init__(self, user_id: str, username: str, email: str, password: str):
        """
        Initialization of the User object
        
        Args:
            user_id (str): Unique identifier for the user
            username (str): Username for authentication
            email (str): Email address of the user
            password (str): Password for user account
            
        Attributes:
            user_id: Unique identifier for the user
            username: Username for authentication
            email: User's email address
            _password: Encrypted or stored password
            _is_logged_in: Boolean flag indicating login status
        """
        
        self.user_id = user_id
        self.username = username
        self.email = email
        self._password = password
        self._is_logged_in = False
    
    
    def login(self, password: str):
        """
        Method to login user with password verification
        
        Args:
            password (str): Password to verify against stored password
        """
        
        if self.check_password(password):
            self._is_logged_in = True
        
    
    def logout(self):
        """
        Method to logout the user
        """
        
        self._is_logged_in = False
    
    
    def check_password(self, password: str) -> bool:
        """
        Method to verify if provided password matches stored password
        
        Args:
            password (str): Password to verify
            
        Returns:
            bool: True if password matches, False otherwise
        """
        
        return self._password == password
    

    @staticmethod
    def to_dict(self) -> dict:
        """
        Method to convert User object to dictionary representation
        
        Returns:
            dict: User object as dictionary with all attributes
        """
        
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "password": self._password,
            "is_logged_in": self._is_logged_in
        }
    
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'User':
        """
        Class method to create User object from dictionary representation
        
        Args:
            data (Dict): Dictionary containing user data
            
        Returns:
            User: New User object created from dictionary data
        """
        
        return cls(
            user_id=data['user_id'],
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
    
    
    @property
    def is_logged_in(self) -> bool:
        """
        Property method to check if user is currently logged in
        
        Returns:
            bool: True if user is logged in, False otherwise
        """
        
        return self._is_logged_in

    
    @property
    def password(self) -> str:
        """
        Property method to retrieve the user's password
        
        Returns:
            str: User's password
        """
        
        return self._password
    
    
    @password.setter
    def password(self, new_password: str):
        """
        Property setter to update the user's password
        
        Args:
            new_password (str): New password to set
        """
        
        self._password = new_password
