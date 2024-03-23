from jose import JWTError, jwt
from dotenv import load_dotenv
import os
from decouple import config
  
JWT_SECRET = config("JWT_SECRET")
JWT_ALGORITHM = config("JWT_ALGORITHM")

def decodeJWT(token: str) -> dict:
    try: 
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token 
    except:
        return {}

def sign_jwt(user_id: str) -> dict[str, str]:
    payload = {
        "user_id": user_id, 
    } 
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return {
        "access_token": token,
        "token_type": 'bearer'
    }