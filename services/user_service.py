from fastapi import FastAPI, Header, HTTPException, Depends

import os
from dotenv import load_dotenv

from utils.mock_data_loader import load_mock_data
from utils.jwt_utils import verify_jwt_token, create_access_token, create_refresh_token

load_dotenv()

SECRET_KEY = os.getenv("USER_SERVICE_SECRET_KEY") #use your own secret key
ALGORITHM = os.getenv("USER_SERVICE_ALGORITHM") #Default JWT algorithm is HS256. You can Use any algorithm you want
user_app = FastAPI()

user_service_url = '/user_service/'

#dependency for verifying JWT
async def authenticate(token: str = Header(...)):
    try:
        verify_jwt_token(
            token=token,
            secret_key=SECRET_KEY,
            algorithm=ALGORITHM
            )
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

@user_app.get("/refresh-token")
async def refresh_token(refresh_token: str = Header(...)):
    try:
        #verify the  refresh token
        payload = verify_jwt_token(
            token=refresh_token,
            secret_key=SECRET_KEY,
            algorithm=ALGORITHM
        )

        # Generate new access token
        new_access_token = create_access_token(
            data={
                "service": "user_service",
                "payload": payload
                },
            secret_key=SECRET_KEY, 
            algorithm=ALGORITHM,
            expires_in=1440 #1 day
        )
        return {'access_token': new_access_token}
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


@user_app.get("/")
async def welcome():
    return {"welcome": "You are in User service's welcome page"}

@user_app.get('/api/user/{user_id}', dependencies=[Depends(authenticate)])
async def single_user(user_id):
    url = user_service_url+str(user_id)+'.json'
    data = load_mock_data(url)
    return data