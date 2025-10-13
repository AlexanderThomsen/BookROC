from typing import List, Optional
from app.models.UserBooks import UserBook, UserBookCreate, UserBookRead
from datetime import datetime
from sqlalchemy.orm import Session
from app.database import SessionLocal



class UserBookService:
    def __init__(self):
        self.db: Session = SessionLocal()

    def create_userbook(self, userbook_data: UserBookCreate) -> UserBookRead:
        """Opret en ny UserBook-relation"""
        new_userbook = UserBook(
            id=self._id_counter,
            user_id=userbook_data.user_id,
            book_id=userbook_data.book_id,
            status=userbook_data.status,
            rating=userbook_data.rating,
            created_at=datetime.utcnow(),
        )
        self._db.append(new_userbook)
        self._id_counter += 1
        return UserBookRead(**new_userbook.to_dict())

    def get_all_userbooks(self) -> List[UserBookRead]:
        return [UserBookRead(**ub.to_dict()) for ub in self._db]

    def get_userbook_by_id(self, userbook_id: int) -> Optional[UserBookRead]:
        ub = next((ub for ub in self._db if ub.id == userbook_id), None)
        return UserBookRead(**ub.to_dict()) if ub else None

    def get_books_by_user(self, user_id: int) -> List[UserBookRead]:
        return [UserBookRead(**ub.to_dict()) for ub in self._db if ub.user_id == user_id]

    def get_users_by_book(self, book_id: int) -> List[UserBookRead]:
        return [UserBookRead(**ub.to_dict()) for ub in self._db if ub.book_id == book_id]

    def update_userbook(self, userbook_id: int, userbook_data: UserBookCreate) -> Optional[UserBookRead]:
        ub = next((ub for ub in self._db if ub.id == userbook_id), None)
        if not ub:
            return None
        ub.status = userbook_data.status
        ub.rating = userbook_data.rating
        ub.updated_at = datetime.utcnow()
        return UserBookRead(**ub.to_dict())

    def delete_userbook(self, userbook_id: int) -> bool:
        global _db
        ub = next((ub for ub in self._db if ub.id == userbook_id), None)
        if not ub:
            return False
        self._db.remove(ub)
        return True
