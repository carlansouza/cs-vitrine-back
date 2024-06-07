from src.modules.car.dto import CarCreate, Car
from src.models.cars_models import Car as CarModel
from src.modules.car import repository

def get_car_by_id(car_id: int):
    return repository.get_car_by_id(car_id)

def create_car(car_data: CarCreate):
    return repository.create_car(car_data)

def update_car(car_id: int, car_data: CarCreate):
    return repository.update_car(car_id, car_data)

def delete_car(car_id: int):
    return repository.delete_car(car_id)

def get_cars():
    return repository.get_cars()