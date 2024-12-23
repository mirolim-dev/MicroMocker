import os, json

MOCK_DATA_PATH = os.path.join(os.path.dirname(__file__), 'mock_data')

def load_mock_data(external_url:str):
    """
    MOCK_DATA_PATH: mock_data #the folder that is all services mock API(json) data located.

    external_url: It is a location of file inside of mock_data. Remember!! while taking it mock_data's url already taken which is storing all services FakeAPI data
    """
    actual_url = MOCK_DATA_PATH+external_url
    try:
        with open(actual_url, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"Error": f"{actual_url} not found."}
    except json.JSONDecodeError:
        data = {"Error" : "Failed to decode JSON."}
    return data