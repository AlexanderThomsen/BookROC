import os
import requests
from datetime import datetime, timezone
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from book import Book, Base

API_KEY = os.getenv("NYT_BOOKS_API_KEY")
URL = "https://api.nytimes.com/svc/books/v3/lists/overview.json"

DB_NAME = os.getenv("DB_NAME", "BookROC")
DATABASE_URL = f"mssql+pyodbc://(LocalDB)\\MSSQLLocalDB/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, future=True)

def fetch_books():
    print("📚 Henter NYT Books data...")
    response = requests.get(URL, params={"api-key": API_KEY})
    response.raise_for_status()

    data = response.json()
    session = SessionLocal()

    try:
        for book_list in data["results"]["lists"]:
            genre = book_list["list_name"]
            for b in book_list["books"]:
                isbn = b["primary_isbn13"]

                # Undgå duplikater
                existing = session.query(Book).filter_by(ISBN=isbn).first()
                if existing:
                    continue

                book = Book(
                    Title=b["title"],
                    Author=b["author"],
                    PublishedYear=None,
                    Rating=None,
                    ISBN=isbn,
                    Genre=genre,
                    Description=b.get("description", ""),
                    Created_At=datetime.now(timezone.utc),
                    Updated_At=datetime.now(timezone.utc)
                )
                session.add(book)

        session.commit()
        print(f"✅ Færdig – gemte nye bøger i databasen")
    except Exception as e:
        session.rollback()
        print(f"❌ Fejl under gemning: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    fetch_books()
