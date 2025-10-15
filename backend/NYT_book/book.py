from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Book(Base):
    __tablename__ = "Books"

    BookID = Column(Integer, primary_key=True, autoincrement=True)
    Title = Column(String(255), nullable=False)
    Author = Column(String(255), nullable=False)
    PublishedYear = Column(Integer, nullable=True)
    Rating = Column(Float, nullable=True)
    ISBN = Column(String(50), unique=True, index=True)
    Genre = Column(String(100), nullable=True)
    Description = Column(String(1000), nullable=True)
    Created_At = Column(DateTime, default=datetime.utcnow)
    Updated_At = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
