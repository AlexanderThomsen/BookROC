from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

# -------------------------------------
# SQLAlchemy Base
# -------------------------------------
Base = declarative_base()

# -------------------------------------
# Dataklasse / ORM model
# -------------------------------------
@dataclass
class User(Base):
    __tablename__ = "Users"  # Bemærk stort 'U', matcher SQL Server
    
    UserID = Column(Integer, primary_key=True, autoincrement=True)
    UserName = Column(String(50), nullable=False)
    Email = Column(String(100), nullable=False, unique=True)
    Password_Hash = Column(String(255), nullable=False)
    Created_At = Column(DateTime, default=datetime.utcnow)
    Updated_At = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "UserID": self.UserID,
            "UserName": self.UserName,
            "Email": self.Email,
            "Created_At": self.Created_At.isoformat() if self.Created_At else None,
            "Updated_At": self.Updated_At.isoformat() if self.Updated_At else None,
        }

# -------------------------------------
# Pydantic modeller til API
# -------------------------------------

# Input-model: bruges når klient opretter en bruger
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str  # Gemmes krypteret i service/DB

# Output-model: bruges når vi returnerer en bruger fra API
class UserRead(BaseModel):
    userid: int
    username: str
    email: EmailStr
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
