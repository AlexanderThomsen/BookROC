from fastapi import APIRouter, HTTPException, status
from typing import List

from app.models.UserBooks import UserBookCreate, UserBookRead
from app.services.UserBooks import UserBookService

router = APIRouter(prefix="/userbooks", tags=["UserBooks"])

userbook_service = UserBookService()


@router.post("/", response_model=UserBookRead, status_code=status.HTTP_201_CREATED)
def create_userbook(userbook_data: UserBookCreate):
    """Opret en relation mellem bruger og bog"""
    userbook = userbook_service.create_userbook(userbook_data)
    return userbook


@router.get("/", response_model=List[UserBookRead])
def list_userbooks():
    """Hent alle relationer mellem brugere og bøger"""
    return userbook_service.get_all_userbooks()


@router.get("/{userbook_id}", response_model=UserBookRead)
def get_userbook(userbook_id: int):
    """Hent en specifik relation ud fra ID"""
    userbook = userbook_service.get_userbook_by_id(userbook_id)
    if not userbook:
        raise HTTPException(status_code=404, detail="UserBook relation not found")
    return userbook


@router.get("/user/{user_id}", response_model=List[UserBookRead])
def get_books_for_user(user_id: int):
    """Hent alle bøger tilknyttet en bestemt bruger"""
    return userbook_service.get_books_by_user(user_id)


@router.get("/book/{book_id}", response_model=List[UserBookRead])
def get_users_for_book(book_id: int):
    """Hent alle brugere der har tilknyttet en bestemt bog"""
    return userbook_service.get_users_by_book(book_id)


@router.put("/{userbook_id}", response_model=UserBookRead)
def update_userbook(userbook_id: int, userbook_data: UserBookCreate):
    """Opdater status eller rating for en relation"""
    userbook = userbook_service.update_userbook(userbook_id, userbook_data)
    if not userbook:
        raise HTTPException(status_code=404, detail="UserBook relation not found")
    return userbook


@router.delete("/{userbook_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_userbook(userbook_id: int):
    """Slet en relation"""
    success = userbook_service.delete_userbook(userbook_id)
    if not success:
        raise HTTPException(status_code=404, detail="UserBook relation not found")
    return None
