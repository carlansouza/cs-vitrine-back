from fastapi import  FastAPI
from src.modules.user.router import router as user_router
from src.modules.auth.router import router as auth_router
from src.modules.car.router import router as car_router
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
import os


port = os.environ.get('PORT') or 8000;

app = FastAPI(
    title="CSCar Backend API",
    description="CSCar Project API documentation",
    version="0.0.1",
    debug=True,
)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Métodos permitidos
    allow_headers=["*"]
)

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(car_router)

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
