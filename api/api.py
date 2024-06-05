from fastapi import  FastAPI
from src.modules.user.router import router as user_router
from src.modules.auth.router import router as auth_router
from src.modules.car.router import router as car_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="CSCar Backend API",
    description="CSCar Project API documentation",
    version="0.0.1",
    debug=True,
)

origins = [
    "https://cs-vitrine-back-445greuix-carlas-projects-420903b3.vercel.app/ping"
    # "http://localhost",
    # "http://localhost:8000",
    # "http://localhost:4200"
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

