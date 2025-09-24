from fastapi import APIRouter, HTTPException
from app.models.User import UserCreate, UserRead
from app.services.UserService import UserService

router = APIRouter()
service = UserService()

@router.post("/", response_model=UserRead, summary="Opret en ny bruger")
def create_user(user: UserCreate):
    return service.create_user(user)

@router.get("/{user_id}", response_model=UserRead, summary="Hent en bruger efter ID")
def get_user(user_id: int):
    user = service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
