import time
import os
import jwt
from pathlib import Path

from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from .settings.secret_configs import get_secret


BASE_DIR = Path(__file__).resolve().parent.parent
JWT_PRIVATE_KEY_PATH = get_secret('JWT_PRIVATE_KEY_PATH')
JWT_PUBLIC_KEY_PATH = get_secret('JWT_PUBLIC_KEY_PATH')
JWT_ALGORITHM = get_secret("JWT_ALGORITHM")

private_key_path = os.path.join(BASE_DIR, JWT_PRIVATE_KEY_PATH)
public_key_path = os.path.join(BASE_DIR, JWT_PUBLIC_KEY_PATH)

with open(private_key_path, 'rb') as public_key_file:
    private_key = public_key_file.read().decode("utf-8")

with open(public_key_path, 'rb') as public_key_file:
    public_key = public_key_file.read().decode("utf-8")


def signJWT(user_id: str) -> str:
    payload = {
        "user_id": user_id,
        "exp": time.time() + 600
    }

    token = jwt.encode(payload=payload, key=private_key, algorithm=JWT_ALGORITHM)
    return token


def refreshJWT(user_id: str) -> str:
    payload = {
        "user_id": user_id,
        "exp": time.time() + 600
    }
    token = jwt.encode(payload, private_key, algorithm=JWT_ALGORITHM)

    return token


def decodeJWT(token: str) -> dict:
    try:

        decoded_token = jwt.decode(token, public_key, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["exp"] >= time.time() else None
    except:
        return {}


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            # print(credentials.credentials)
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid


""""
# Generate private key
openssl genrsa -out private.pem 2048
# Extract public key from it
openssl rsa -in private.pem -pubout > public.pem
"""
