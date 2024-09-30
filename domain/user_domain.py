from infrastructure.repositories import Repositories
import bcrypt
import jwt
from config import JWT_SECRET
from presentation.responses.response_data.login_response_data import LoginResponseData
from .entities.user import User

class UserDomain:
    def __init__(self) -> None:
        self.repository = Repositories.USER_REPOSITORY

    def authorize(self, auth: str) -> str | None:
        try:
            data = jwt.decode(auth, JWT_SECRET, algorithms=["HS256"])
            if not data: return None
            return data.get("id")
        except Exception as e:
            print(e, type(e))
            return None

    def login(self, username: str, password: str) -> LoginResponseData:
        password_bytes = password.encode()
        user = self.repository.get_user_from_username(username)
        if not user:
            raise ValueError("User not found")
        if not bcrypt.checkpw(password_bytes, user.password):
            raise ValueError("User not found")
        encoded = jwt.encode({"id": user.username}, JWT_SECRET)
        return LoginResponseData(authentication_token=encoded)
    
    def register(self, username: str, password: str) -> LoginResponseData:
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user = User(username, hashed_pw)
        self.repository.add_user(user)
        encoded = jwt.encode({"id": user.username}, JWT_SECRET)
        return LoginResponseData(authentication_token=encoded)
        

