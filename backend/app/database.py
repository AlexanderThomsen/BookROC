import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import urllib

DB_SERVER = os.getenv("DB_SERVER")
DB_NAME = os.getenv("DB_NAME")
DB_DRIVER = os.getenv("DB_DRIVER")

if not all([DB_SERVER, DB_NAME, DB_DRIVER]):
    missing = [v for v in ["DB_SERVER","DB_NAME","DB_DRIVER"] if not os.getenv(v)]
    raise ValueError(f"Mangler miljøvariabler: {', '.join(missing)}")

driver_encoded = urllib.parse.quote_plus(DB_DRIVER)

DATABASE_URL = f"mssql+pyodbc://{DB_SERVER}/{DB_NAME}?driver={driver_encoded}&trusted_connection=yes"

engine = create_engine(DATABASE_URL, echo=True, future=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, future=True)

Base = declarative_base()
