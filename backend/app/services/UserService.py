from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.User import User

class UserService:
    def __init__(self):
        self.db: Session = SessionLocal()

    def get_all_users(self):
        """Hent alle brugere"""
        return self.db.query(User).all()

    def get_user_by_id(self, user_id: int):
        """Hent en bruger via ID"""
        return self.db.query(User).filter(User.UserID == user_id).first()

    def create_user(self, username: str, email: str, password: str):
        """Opret en ny bruger"""
        new_user = User(
            UserName=username,
            Email=email,
            Password_Hash=password
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def update_user(self, user_id: int, **kwargs):
        """Opdater en eksisterende bruger dynamisk via kwargs"""
        user = self.get_user_by_id(user_id)
        if not user:
            return None
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, user_id: int):
        """Slet en bruger"""
        user = self.get_user_by_id(user_id)
        if not user:
            return False
        self.db.delete(user)
        self.db.commit()
        return True

    def __del__(self):
        self.db.close()
