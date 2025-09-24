from fastapi import FastAPI
from app.routes.UserController import router as user_router
# from app.routes.BookController import router as book_router
# from app.routes.UserBookController import router as userbook_router

app = FastAPI(title="BookROC API", version="1.0")

# Inkluder alle routers
app.include_router(user_router, prefix="/users", tags=["Users"])
# app.include_router(book_router, prefix="/books", tags=["Books"])
# app.include_router(userbook_router, prefix="/userbooks", tags=["UserBooks"])
