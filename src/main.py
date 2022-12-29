from fastapi import FastAPI, HTTPException, Depends
import uvicorn
from typing import List
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from model import Base
from crud import get_customers,get_customer_details,add_customer
from schema import CustomerBase,CustomerCreateBase

# initilize db
Base.metadata.create_all(bind=engine)

app = FastAPI()

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# handle get customers
@app.get("/", response_model=List[CustomerBase])
def index(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    customers_list = get_customers(db,skip,limit)
    return customers_list



# handle get customer details
@app.get("/{customer_id}", response_model=CustomerBase)
def handle_get_customer_details(customer_id: int, db: Session = Depends(get_db)):
    customer_details = get_customer_details(db, customer_id)
    if customer_details is None:
        raise HTTPException(status_code=404, detail="Customer not found..")
    return customer_details



# add new customer
@app.post("/add", response_model=CustomerBase)
def handle_add_customer(customer: CustomerCreateBase, db: Session = Depends(get_db)):
    return add_customer(db, customer)

