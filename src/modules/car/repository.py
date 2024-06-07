from src.modules.database.db_connection import SessionLocal
from src.modules.car.dto import CarCreate, Car
from src.models.cars_models import Car as CarModel

def get_car_by_id(car_id: int):
    session = SessionLocal()
    car = session.query(CarModel).filter(CarModel.id == car_id).first()
    session.close()
    return car

def create_car(car_data: CarCreate):
    session = SessionLocal()
    car = CarModel(**car_data.dict())
    session.add(car)
    session.commit()
    session.refresh(car)
    session.close()
    return car

def update_car(car_id: int, car_data: CarCreate):
    session = SessionLocal()
    car = session.query(CarModel).filter(CarModel.id == car_id).first()
    for key, value in car_data.dict().items():
        setattr(car, key, value)
    session.commit()
    session.refresh(car)
    session.close()
    return car

def delete_car(car_id: int):
    session = SessionLocal()
    car = session.query(CarModel).filter(CarModel.id == car_id).first()
    session.delete(car)
    session.commit()
    session.close()
    
def get_cars():
    session = SessionLocal()
    cars = session.query(CarModel).all()
    session.close()
    return cars
