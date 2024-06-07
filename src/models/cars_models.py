from sqlalchemy import Column, Integer, String
from src.modules.database.db_connection import Base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

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
    d_alt = Column(String)

    
