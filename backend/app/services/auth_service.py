# app/services/auth_service.py
import requests
from app.models.User import User

GOOGLE_CLIENT_ID = "848574082823-qnp6crcb4l3si2sp37rgcnaf2c44gm0q.apps.googleusercontent.com"

class AuthService:
    @staticmethod
    def verify_google_token(token: str) -> User:
        """
        Verificér token hos Google og returnér en User
        """
        response = requests.get(f"https://oauth2.googleapis.com/tokeninfo?id_token={token}")
        id_info = response.json()

        if id_info.get("aud") != GOOGLE_CLIENT_ID:
            raise ValueError("Ugyldig client ID")

        user = User(
            sub=id_info.get("sub"),
            email=id_info.get("email"),
            name=id_info.get("name"),
            picture=id_info.get("picture")
        )
        return user
