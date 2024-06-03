from src.modules.database.db_connection import SessionLocal
from src.models.users_model import User as UserModel
from src.modules.user.dto import User

def get_all_users(page: int = 1, per_page: int = 10):
    session = SessionLocal()
    data = session.query(UserModel).offset((page - 1) * per_page).limit(per_page).all()
    data = [
        User(id=user.id, 
            name=user.name,
            email=user.email,
            is_active=user.is_active,
            created_at=user.created_at,
            updated_at=user.updated_at,
            role=user.role,
        ) for user in data
    ]
    session.close()
    return data

def get_total_users_count():
    session = SessionLocal()
    total_users = session.query(UserModel).count()
    session.close()
    return total_users

def get_user_by_id(user_id: int):
    session = SessionLocal()
    user = session.query(UserModel).filter(UserModel.id == user_id).first()
    if user:
        data = User(id=user.id, 
                    name=user.name,
                    email=user.email,
                    is_active=user.is_active,
                    created_at=user.created_at,
                    updated_at=user.updated_at,
                    role=user.role,
                    )
    else:
        data = None
    session.close()
    return data

def create_user(user):
    session = SessionLocal()
    session.add(user)
    session.commit()
    session.refresh(user)
    del user.hashed_password
    return user


def delete_user(user_id: int):
    session = SessionLocal()
    user = session.query(UserModel).filter(UserModel.id == user_id).first()
    session.delete(user)
    session.commit()
    return user
    
def get_user_by_email(email: str):
    session = SessionLocal()
    user = session.query(UserModel).filter(UserModel.email == email).first()
    if user:
        data = user
    else:
        data = None
    session.close()
    return data