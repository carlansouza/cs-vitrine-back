from passlib.context import CryptContext
from src.modules.user.dto import UserCreate
from src.modules.user import repository
from src.models.users_model import User as UserModel

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_all_users(page: int = 1, per_page: int = 10):
    return repository.get_all_users(page=page, per_page=per_page)

def get_total_users_count():
    return repository.get_total_users_count()


def get_user_by_id(user_id: int):
    return repository.get_user_by_id(user_id)                                

def create_user(user: UserCreate):
    hashed_password = pwd_context.hash(user.hashed_password)
    user_data = UserModel(name=user.name, 
                          email=user.email, 
                          hashed_password=hashed_password)
    return repository.create_user(user_data) 

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def delete_user(user_id: int):
    return repository.delete_user(user_id)

def get_user_by_email(email: str):
    return repository.get_user_by_email(email)

