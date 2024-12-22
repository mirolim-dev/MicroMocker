from fastapi import FastAPI

from mock_data_loader import load_mock_data

user_app = FastAPI()

user_service_url = '/user_service/'

@user_app.get("/")
async def welcome():
    return {"welcome": "You are in User service's welcome page"}

@user_app.get('/api/user/{user_id}')
async def single_user(user_id):
    url = user_service_url+str(user_id)+'.json'
    data = load_mock_data(url)
    return data