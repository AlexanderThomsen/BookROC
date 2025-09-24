from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

# -------------------------------------
# Dataklasse (intern repræsentation)
# -------------------------------------
@dataclass
class User:
    user_id: int
    username: str
    email: str
    password_hash: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    is_active: bool = True

    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "is_active": self.is_active,
        }

# -------------------------------------
# Pydantic-modeller til API
# -------------------------------------

# Input-model: bruges når klient opretter en bruger
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str  # Gemmes krypteret i service/DB

# Output-model: bruges når vi returnerer en bruger fra API
class UserRead(BaseModel):
    user_id: int
    username: str
    email: EmailStr
    created_at: datetime
    updated_at: Optional[datetime] = None
    is_active: bool

    class Config:
        orm_mode = True
