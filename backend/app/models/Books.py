from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"

    BookID = Column(Integer, primary_key=True, index=True)
    Title = Column(String(255), nullable=False)
    Author = Column(String(255), nullable=True)
    PublishedYear = Column(Integer, nullable=True)
    Rating = Column(Float, nullable=True)
    ImageUrl = Column(String(500), nullable=True)  # <-- Tilføjet
    Created_At = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    Updated_At = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict:
        return {
            "book_id": self.BookID,
            "title": self.Title,
            "author": self.Author,
            "published_year": self.PublishedYear,
            "rating": self.Rating,
            "image_url": self.ImageUrl,
            "created_at": self.Created_At.isoformat(),
            "updated_at": self.Updated_At.isoformat() if self.Updated_At else None,
        }

# -------------------------------------
# Pydantic-modeller til API
# -------------------------------------

class BookCreate(BaseModel):
    Title: str
    Author: Optional[str] = None
    PublishedYear: Optional[int] = None
    Rating: Optional[float] = None
    ImageUrl: Optional[str] = None  # <-- Tilføjet

class BookRead(BaseModel):
    BookID: int
    Title: str
    Author: Optional[str] = None
    PublishedYear: Optional[int] = None
    Rating: Optional[float] = None
    ImageUrl: Optional[str] = None  # <-- Tilføjet
    Created_At: datetime
    Updated_At: Optional[datetime] = None

    class Config:
        orm_mode = True
