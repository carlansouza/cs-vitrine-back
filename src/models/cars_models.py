from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from src.modules.database.db_connection import Base

class Car(Base):
    """
    Car model class for storing user related details
    """
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, index=True)
    model = Column(String, index=True)
    
