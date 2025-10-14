from fastapi import APIRouter, HTTPException, status
from typing import List

from app.models.Books import BookCreate, BookRead
from app.services.BookService import BookService

router = APIRouter(prefix="/books", tags=["Books"])

book_service = BookService()


@router.post("/", response_model=BookRead, status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookCreate):
    """Opret en ny bog"""
    book = book_service.create_book(book_data)
    return book


@router.get("/", response_model=List[BookRead])
def list_books():
    """Hent alle bøger"""
    return book_service.get_all_books()


@router.get("/{book_id}", response_model=BookRead)
def get_book(book_id: int):
    """Hent en enkelt bog ud fra ID"""
    book = book_service.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/{book_id}", response_model=BookRead)
def update_book(book_id: int, book_data: BookCreate):
    """Opdater en eksisterende bog"""
    book = book_service.update_book(book_id, book_data)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    """Slet en bog"""
    success = book_service.delete_book(book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return None
