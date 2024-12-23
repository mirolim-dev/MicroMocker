import jwt
import datetime
from typing import Dict

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440  # 1 Day = 1440 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 43200  # 30 Days = 43200 minutes

def create_access_token(data: Dict, secret_key:str, algorithm:str = ALGORITHM, expires_in: int = ACCESS_TOKEN_EXPIRE_MINUTES):
    """
    Generates Access token to each server by their secret_key, Algorithm.
        data: payload data to encode.
        secret_key: specific secret key for service.
        algorithm: hashing algorithm to secure data.
        iss: Issuer service.
        expires_in: Token expiry time by minutes.
        return: Encoded jwt token.
    """
    payload = data.copy()
    payload.update({
        "exp": datetime.datetime.now(datetime.timezone.utc()) + datetime.timedelta(minutes=expires_in),
        "iat": datetime.datetime.now(datetime.timezone.utc()),
        "type": "access" #toke type for validation
        })
    token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return token


def create_refresh_token(data: Dict, secret_key:str, algorithm:str = ALGORITHM, expires_in: int = REFRESH_TOKEN_EXPIRE_MINUTES):
    """
    Generates Refresh token to each server by their secret_key, Algorithm.
        data: payload data to encode.
        secret_key: specific secret key for service.
        algorithm: hashing algorithm to secure data.
        iss: Issuer service.
        expires_in: Token expiry time by minutes.
        return: Encoded jwt token.
    """
    payload = data.copy()
    payload.update({
        "exp": datetime.datetime.now(datetime.timezone.utc()) + datetime.timedelta(minutes=expires_in),
        "iat": datetime.datetime.now(datetime.timezone.utc()),
        "type": "refresh" #token type for validation
        })
    token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return token


def verify_jwt_token(token: str, secret_key:str, algorithm:str=ALGORITHM):
    """
    Verifies JWT token.
        token: Encoded JWT token.
        secret_key: specific secret key for service.
        algorithm: hashing algorithm to secure data.
        return: Decoded payload if token is valid, raises an exeption if token is invalid.
    """
    try: 
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token has been expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")