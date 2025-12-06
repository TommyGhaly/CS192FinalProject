# Main User Class
class User:
    def __int__(self, user_id:str, username:str, email:str, password:str ):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.is_logged_in = False
    
    
    def login(self):
        self.is_logged_in = True
        
    
    def logout(self):
        self.is_logged_in = False
    
    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }
    
    def from_dict(data:dict) -> 'User':
        return User(
            user_id=data['user_id'],
            username=data['username'],
            email=data['email'],
            password=data['password']
        )