from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

from sqlalchemy import Column, String, Integer, DateTime

class Book(Base):
    __tablename__ = "Books"

    BookID = Column(Integer, primary_key=True, autoincrement=True)
    Title = Column(String(255))
    Author = Column(String(255))
    PublishedYear = Column(Integer, nullable=True)
    Rating = Column(Integer, nullable=True)
    ISBN = Column(String(20), unique=True)
    Genre = Column(String(100))
    Description = Column(String(1000))
    ImageUrl = Column(String(500), nullable=True)  # <-- ny kolonne
    Created_At = Column(DateTime)
    Updated_At = Column(DateTime)
