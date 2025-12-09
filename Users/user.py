from typing import Type, Dict
# Main User Class
class User:
    def __init__(self, user_id:str, username:str, email:str, password:str ):
        self.user_id = user_id
        self.username = username
        self.email = email
        self._password = password
        self._is_logged_in = False
    
    
    def login(self, password:str):
        if self.check_password(password):
            self._is_logged_in = True
        
    
    def logout(self):
        self._is_logged_in = False
    
    def check_password(self, password:str) -> bool:
        return self._password == password
    

    @staticmethod
    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "password": self._password,
            "is_logged_in": self._is_logged_in
        }
    
    @classmethod
    def from_dict(cls: Type['User'], data:Dict) -> 'User':
        return cls(
            user_id=data['user_id'],
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
    
    
    @property
    def is_logged_in(self) -> bool:
        return self._is_logged_in

    @property
    def password(self) -> str:
        return self._password
    
    @password.setter
    def password(self, new_password:str):
        self._password = new_password
