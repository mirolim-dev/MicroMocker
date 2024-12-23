import jwt
import datetime
from typing import Dict

import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY") #use your own secret key
ALGORITHM = os.getenv("ALGORITHM") #Default JWT algorithm is HS256. You can Use any algorithm you want

def create_jwt_token(secret_key:str, algorithm:str, iss:str, data: Dict, expires_in: int = 60):
    """
    Generates JWT token to each server by their secret_key, Algorithm.
        secret_key: specific secret key for service.
        algorithm: hashing algorithm to secure data.
        iss: Issuer service.
        data: payload data to encode.
        expires_in: Token expiry time by minutes.
        return: Encoded jwt token.
    """
    payload = data.copy()
    payload.update({
        "exp": datetime.datetime.now(datetime.timezone.utc()) + datetime.timedelta(minutes=expires_in),
        "iss": iss #Issuer service
        })
    token = jwt.encode(payload, secret_key, algorithm=algorithm)

    return token


# def create_jwt_token(data: Dict, expires_in: int = 60):
#     """
#     Generates JWT token.
#         data: payload data to encode.
#         expires_in: Token expiry time by minutes.
#         return: Encoded jwt token.
#     """
#     payload = data.copy()
#     payload.update({"exp": datetime.datetime.now(datetime.timezone.utc()) + datetime.timedelta(minutes=expires_in)})
#     token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

#     return token


# def verify_jwt_token(token: str):
#     """
#     Verifies JWT token.
#         token: Encoded JWT token.
#         return: Decoded payload if token is valid, raises an exeption if token is invalid.
#     """
#     try: 
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return payload
#     except jwt.ExpiredSignatureError:
#         raise Exception("Token has been expired")
#     except jwt.InvalidTokenError:
#         raise Exception("Invalid token")
    
def verify_jwt_token(secret_key:str, algorithm:str, iss:str, token: str):
    """
    Verifies JWT token.
        secret_key: specific secret key for service.
        algorithm: hashing algorithm to secure data.
        iss: Issuer service.
        token: Encoded JWT token.
        return: Decoded payload if token is valid, raises an exeption if token is invalid.
    """
    try: 
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        if payload.get('iss') != iss:
            raise Exception("Invalid token issuer")
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token has been expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")