from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# -------------------------------------
# Dataklasse (intern repræsentation)
# -------------------------------------
@dataclass
class Book:
    book_id: int
    title: str
    author: Optional[str] = None
    published_year: Optional[int] = None
    rating: Optional[float] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None

    def to_dict(self) -> dict:
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "published_year": self.published_year,
            "rating": self.rating,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

# -------------------------------------
# Pydantic-modeller til API
# -------------------------------------

# Input-model: bruges når klient opretter en bog
class BookCreate(BaseModel):
    title: str
    author: Optional[str] = None
    published_year: Optional[int] = None
    rating: Optional[float] = None  # Kan evt. udfyldes senere

# Output-model: bruges når vi returnerer en bog fra API
class BookRead(BaseModel):
    book_id: int
    title: str
    author: Optional[str] = None
    published_year: Optional[int] = None
    rating: Optional[float] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
