from fastapi import FastAPI, Header, HTTPException, Depends
import os
from dotenv import load_dotenv

load_dotenv()

from utils.mock_data_loader import load_mock_data
from utils.jwt_utils import verify_jwt_token

vehicle_app = FastAPI()

SECRET_KEY = os.getenv("VEHICLE_SERVICE_SECRET_KEY")
ALGORITHM = os.getenv("VEHICLE_SERVICE_ALGORITHM")

vehicle_service_url = '/vehicle_service/vehicle/'
# a3f9b1c6-5e2f-4d3a-b6f9-2c7a1d5b4e7a
firm_service_url = '/vehicle_service/firm/'

#dependency for vehicle JWT
async def authenticate(token:str = Header(...)):
    try:
        verify_jwt_token(
            token=token,
            secret_key=SECRET_KEY,
            algorithm=ALGORITHM
            )
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


@vehicle_app.get("/")
async def welcome():
    return {"welcome": "You are in Vehicle service's welcome page"}

@vehicle_app.get('/api/vehicle/{vehicle_id}', dependencies=[Depends(authenticate)])
async def single_vehicle(vehicle_id):
    url = vehicle_service_url+str(vehicle_id)+'.json'
    data = load_mock_data(url)
    return data


@vehicle_app.get('/api/firm/{firm_id}', dependencies=[Depends(authenticate)])
async def single_firm(firm_id):
    url = firm_service_url+str(firm_id)+'.json'
    data = load_mock_data(url)
    return data
