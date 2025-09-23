import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))

try:
    DB_SERVER = os.getenv("DB_SERVER")
    DB_NAME = os.getenv("DB_NAME")
    DB_DRIVER = os.getenv("DB_DRIVER")

    DATABASE_URL = f"mssql+pyodbc://@{DB_SERVER}/{DB_NAME}?driver={DB_DRIVER}&trusted_connection=yes"

    engine = create_engine(DATABASE_URL, echo=True)

    Base = declarative_base()

    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
except Exception as ex:
    print(f"exception in database.py: {ex}")