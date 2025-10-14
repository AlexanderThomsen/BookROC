from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.UserService import UserService
from app.utils.token import create_access_token
import requests

router = APIRouter(prefix="/auth", tags=["Auth"])
service = UserService()

GOOGLE_CLIENT_ID = "848574082823-qnp6crcb4l3si2sp37rgcnaf2c44gm0q.apps.googleusercontent.com"

class LoginRequest(BaseModel):
    email: str
    password: str

class GoogleLoginRequest(BaseModel):
    token: str

# Dit eksisterende login
@router.post("/login")
def login(data: LoginRequest):
    user = service.authenticate_user(data.email, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(user.UserID)})
    return {"access_token": token, "token_type": "bearer"}

# Nyt endpoint til Google login
@router.post("/google")
def google_login(data: GoogleLoginRequest):
    token = data.token

    try:
        # Verificér token hos Google
        response = requests.get(f"https://oauth2.googleapis.com/tokeninfo?id_token={token}")
        id_info = response.json()

        if id_info.get("aud") != GOOGLE_CLIENT_ID:
            raise HTTPException(status_code=400, detail="Ugyldig client ID")

        email = id_info.get("email")
        name = id_info.get("name")
        sub = id_info.get("sub")
        picture = id_info.get("picture")

        # Tjek om brugeren allerede findes i din DB
        user = service.get_user_by_email(email)
        if not user:
            # Gem Google bruger med UserName = name og Password_Hash = tom/placeholder
            user = service.create_user(
                username=name,       # her bruger vi UserName
                email=email,
                password="google-oauth"  # placeholder, da Google ikke bruger password
    )

        # Lav JWT token til frontend
        access_token = create_access_token({"sub": str(user.UserID)})
        return {"access_token": access_token, "token_type": "bearer", "user": {
            "email": user.Email,
            "name": user.UserName,
            "picture": getattr(user, "Picture", None)  # Hvis du ikke har picture-felt endnu
        }}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Ugyldig Google token")
