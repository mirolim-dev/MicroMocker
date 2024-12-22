# MicroMocker - Service-to-Service Communication for Microservices
## Tools and Technologies Used

Here are the main tools and technologies used in this project:

- **FastAPI**  
  ![FastAPI](https://img.shields.io/badge/FastAPI-%23FF8C00?style=for-the-badge&logo=fastapi&logoColor=white)

- **Service-to-Service Communication**  
  ![Service-to-Service](https://img.shields.io/badge/Service--to--Service-%2343B02A?style=for-the-badge&logo=git&logoColor=white)

- **JWT Authentication**  
  ![JWT](https://img.shields.io/badge/JWT-%23FF9E00?style=for-the-badge&logo=javascript&logoColor=white)

****
## Introduction

**MicroMocker** is a simple and flexible solution designed for developers working on **microservices** that need to **simulate service-to-service communication** during the development phase. It allows developers to easily mock APIs for different services, including the use of **JWT authentication**, to simulate real-world scenarios in a safe and controlled environment.

This project was built with **FastAPI** and is ideal for those who need to work on their microservices' business logic in parallel, without waiting for actual service endpoints to be implemented.

## Key Features

- **Parallel Development**: Mock multiple services to simulate real communication between them while working on business logic.
- **JWT Authentication**: Supports JWT authentication to mimic secure communication between microservices.
- **Customizable Data**: Provides easy-to-use methods to load custom mock data from JSON files.
- **Service Isolation**: Each service can run on a different port and simulate different service endpoints.

## Architecture

The project consists of multiple services, each running on a different port, and simulating the communication between services. The architecture includes:

- **User Service**: Simulates the user management service.
- **Vehicle Service**: Simulates the vehicle management service.
- **JWT Authentication**: Both services are secured using JWT tokens for communication.

### Mock API Example

- **User Service** (`http://localhost:8001`):
    - `GET /api/user/{user_id}`: Fetches user information from a mock JSON file.
    - Example response:
      ```json
      {
        "user_id": "123",
        "name": "John Doe",
        "email": "johndoe@example.com"
      }
      ```

- **Vehicle Service** (`http://localhost:8002`):
    - `GET /api/vehicle/{vehicle_id}`: Fetches vehicle data from a mock JSON file.
    - Example response:
      ```json
      {
        "vehicle_id": "456",
        "make": "Toyota",
        "model": "Corolla",
        "year": 2020
      }
      ```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mirolim-dev/MicroMocker.git
   ```

2. **Install dependencies**: Make sure you have Python 3.x installed. Then, install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the services:** The project uses `uvicorn` to run FastAPI apps. You can run both services simultaneously by executing the following: 
   ```python main.py```
This will start two services:

- User service: `http://localhost:8001`
- Vehicle service: `http://localhost:8002`
  
4. **Test the endpoints:** After starting the services, you can access the mock endpoints via a browser or tools like Postman or curl:

- `http://localhost:8001/api/user/{user_id}`
- `http://localhost:8002/api/vehicle/{vehicle_id}`
  
