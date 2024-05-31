from src.modules.car.dto import CarCreate, Car
from fastapi import HTTPException, APIRouter
from src.modules.car import  service
from typing import List


BASE_URL = "/cars"
CONTEXT = "Car"
router = APIRouter()

@router.get(BASE_URL , response_model=List[Car], tags=[CONTEXT])
async def get_all_cars():
    try:
        return service.get_cars()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get(BASE_URL + "/{car_id}", response_model=Car, tags=[CONTEXT])
async def get_car_by_id(car_id: int):
    try:
        car = service.get_car_by_id(car_id)
        if not car:
            raise HTTPException(status_code=404, detail="Car not found")
        return car
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error getting car")
    
@router.post(BASE_URL, response_model=Car, tags=[CONTEXT])
async def create_car(car: CarCreate):
    try:
        return service.create_car(car)
    except Exception as e:
        message = "Error creating car"
        raise HTTPException(
            status_code=400, detail=message
        )
    
@router.delete(BASE_URL + "/{car_id}", tags=[CONTEXT])
async def delete_car(car_id: int):
    try:
        service.delete_car(car_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str("Error deleting car"))

@router.put(BASE_URL + "/{car_id}", response_model=Car, tags=[CONTEXT])
async def update_car(car_id: int, car: CarCreate):
    try:
        return service.update_car(car_id, car)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str("Error updating car"))