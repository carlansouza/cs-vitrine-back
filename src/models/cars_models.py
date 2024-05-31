from sqlalchemy import Column, Integer, String
from src.modules.database.db_connection import Base

class Car(Base):
    """
    Car model class for storing user related details
    """
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    brand = Column(String, index=True)
    model = Column(String, index=True)
    price = Column(Integer)
    image = Column(String)
    d_alt = Column(String, default = "img")

    
