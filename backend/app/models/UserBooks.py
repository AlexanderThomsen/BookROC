from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Literal
from pydantic import BaseModel, conint

# -------------------------------------
# Dataklasse (intern repræsentation)
# -------------------------------------
@dataclass
class UserBook:
    id: int
    user_id: int
    book_id: int
    status: Literal["read", "wish", "favorite"]
    rating: Optional[int] = None  # 0-10, gemmes som tinyint i DB
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "book_id": self.book_id,
            "status": self.status,
            "rating": self.rating,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

# -------------------------------------
# Pydantic-modeller til API
# -------------------------------------

# Input-model: bruges når klienten knytter en bog til en bruger
class UserBookCreate(BaseModel):
    user_id: int
    book_id: int
    status: Literal["read", "wish", "favorite"]
    rating: Optional[conint(ge=0, le=10)] = None  # Validerer at rating er 0-10

# Output-model: bruges når vi returnerer relationen fra API
class UserBookRead(BaseModel):
    id: int
    user_id: int
    book_id: int
    status: Literal["read", "wish", "favorite"]
    rating: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
