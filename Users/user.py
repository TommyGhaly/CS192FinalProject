# Main User Class
class User:
    def __int__(self, user_id:str, username:str, email:str, password:str ):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
    
    
    def login(self):
        pass
    
    def logout(self):
        pass
    

    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }