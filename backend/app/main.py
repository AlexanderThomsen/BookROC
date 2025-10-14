# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.UserController import router as user_router
from app.routes.BookController import router as book_router
from app.routes.UserBookController import router as userbook_router
from app.routes.AuthController import router as auth_router

app = FastAPI(title="BookROC API", version="1.0")

# 🚀 Tilføj CORS Middleware - det SKAL være før include_router
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# app/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Eller eksplicit: ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    allow_headers=["*"],
)

# 👇 include routers EFTER CORS er sat op
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(book_router, prefix="/books", tags=["Books"])
app.include_router(userbook_router, prefix="/userbooks", tags=["UserBooks"])
app.include_router(auth_router)
