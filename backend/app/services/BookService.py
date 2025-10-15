from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.Books import Book, BookCreate, BookRead

class BookService:
   def __init__(self):
        self.db: Session = SessionLocal()

   def get_all_books(self) -> list[BookRead]:
     books = self.db.query(Book).all()
     return [BookRead.model_validate(b, from_attributes=True) for b in books]

   def get_book_by_id(self, book_id: int) -> BookRead | None:
     book = self.db.query(Book).filter(Book.BookID == book_id).first()
     return BookRead.model_validate(book, from_attributes=True) if book else None

   def create_book(self, book_data: BookCreate) -> BookRead:
        new_book = Book(
            Title=book_data.Title,
            Author=book_data.Author,
            PublishedYear=book_data.PublishedYear,
            Rating=book_data.Rating,
        )
        self.db.add(new_book)
        self.db.commit()
        self.db.refresh(new_book)
        return BookRead.model_validate(new_book)

   def update_book(self, book_id: int, **kwargs) -> BookRead | None:
        book = self.db.query(Book).filter(Book.BookID == book_id).first()
        if not book:
            return None
        for key, value in kwargs.items():
            if value is not None and hasattr(book, key):
                setattr(book, key, value)
        self.db.commit()
        self.db.refresh(book)
        return BookRead.model_validate(book)

   def delete_book(self, book_id: int) -> bool:
        book = self.db.query(Book).filter(Book.BookID == book_id).first()
        if not book:
            return False
        self.db.delete(book)
        self.db.commit()
        return True

   def __del__(self):
        self.db.close()
