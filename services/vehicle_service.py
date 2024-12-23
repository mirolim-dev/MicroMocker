from fastapi import FastAPI

from utils.mock_data_loader import load_mock_data

vehicle_app = FastAPI()

vehicle_service_url = '/vehicle_service/vehicle/'
# a3f9b1c6-5e2f-4d3a-b6f9-2c7a1d5b4e7a
firm_service_url = '/vehicle_service/firm/'

@vehicle_app.get("/")
async def welcome():
    return {"welcome": "You are in Vehicle service's welcome page"}

@vehicle_app.get('/api/vehicle/{vehicle_id}')
async def single_vehicle(vehicle_id):
    url = vehicle_service_url+str(vehicle_id)+'.json'
    data = load_mock_data(url)
    return data


@vehicle_app.get('/api/firm/{firm_id}')
async def single_firm(firm_id):
    url = firm_service_url+str(firm_id)+'.json'
    data = load_mock_data(url)
    return data
