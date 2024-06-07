from pydantic import BaseModel

class CarCreate(BaseModel):
    name: str
    brand: str
    model: str
    price: float
    image: str
    d_alt: str

class Car(CarCreate):
    id: int
  
    class Config:
        # orm_mode = True
        from_attributes = True