from sqlalchemy import Column,Integer,String
from database import Base

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer,primary_key=True)
    email = Column(String,unique=True,index=True)
    name = Column(String)