# Main User Class
class User:
    def __init__(self, user_id:str, username:str, email:str, password:str ):
        self._user_id = user_id
        self._username = username
        self._email = email
        self.__password = password
        self._is_logged_in = False
    
    
    def login(self):
        self.is_logged_in = True
        
    
    def logout(self):
        self.is_logged_in = False
    
    def to_dict(self) -> dict:
        return {
            "user_id": self._user_id,
            "username": self._username,
            "email": self._email,
            "password": self.__password
        }
    
    def from_dict(data:dict) -> 'User':
        return User(
            user_id=data['user_id'],
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
    
    
    @property
    def user_id(self) -> str:
        return self._user_id
    
    @property
    def username(self) -> str:
        return self._username
    
    @property
    def email(self) -> str:
        return self._email
    
    @user_id.setter
    def user_id(self, value:str):
        self._user_id = value
    
    @username.setter
    def username(self, value:str):
        self._username = value
    
    @email.setter
    def email(self, value:str):
        self._email = value