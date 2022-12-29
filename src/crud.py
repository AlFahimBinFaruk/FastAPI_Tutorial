from sqlalchemy.orm import Session
from model import Customer
from schema import CustomerCreateBase

# get all customers
def get_customers(db:Session,skip:int=0,limit:int=10):
    return db.query(Customer).offset(skip).limit(limit).all()

# get customer details
def get_customer_details(db:Session,customer_id:int):
    return db.query(Customer).filter(Customer.id==customer_id).first()

# add new customer
def add_customer(db:Session,customer:CustomerCreateBase):
    new_customer = Customer(email=customer.email,name=customer.name) 
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer   

