# app/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ------------------------------
# LocalDB connection der virker
# ------------------------------
DB_NAME = os.getenv("DB_NAME", "BookROC")

# Denne connection string virker med din LocalDB
DATABASE_URL = f"mssql+pyodbc://(LocalDB)\\MSSQLLocalDB/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"

print(f"[DEBUG] Using DATABASE_URL: {DATABASE_URL}")

# Opret engine
engine = create_engine(DATABASE_URL, echo=True, future=True)

# ------------------------------
# SQLAlchemy session & base
# ------------------------------
SessionLocal = sessionmaker(bind=engine, autoflush=False, future=True)
Base = declarative_base()

# Test connection ved startup
try:
    with engine.connect() as conn:
        print("[SUCCESS] Database connection verified!")
except Exception as e:
    print(f"[ERROR] Database connection failed: {e}")
    raise