from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.Books import Book

class BookService():
   def __init__(self):
      self.db: Session = SessionLocal()

   def get_all_books(self):
      """Get all books"""
      return self.db.query(Book).all()
   
   def get_book_by_id(self, book_id: int):
      """Get book by an ID"""
      return self.db.query(Book).filter(Book.book_id == book_id).first()
   
   def create_book(self, title: str, author: str = None, published_year: int = None, rating: float = None):
      """Add a book to the collection"""
      new_book = Book(
         Title = title,
         Author = author,
         PublishedYear =published_year,
         Rating = rating
      )
      self.db.add(new_book)
      self.db.commit()
      self.db.refresh(new_book)
      return new_book
   
   def update_book(self, book_id: int, **kwargs):
      """Opdate a already existing book"""
      book = self.get_book_by_id(book_id)
      if not book:
         return None
      for key, value in kwargs.items():
         if hasattr(book, key):
            setattr(book, key, value)
      self.db.commit()
      self.db.refresh(book)
      return book
   
   def delete_book(self, book_id: int):
      """Delete a already exsisting book"""
      book = self.get_book_by_id(book_id)
      if not book:
         return False
      self.db.delete(book)
      self.db.commit()
      return True
   
   def __del__(self):
      self.db.close()