from pydantic import BaseModel


class CustomerCreateBase(BaseModel):
    name:str
    email:str

class CustomerBase(BaseModel):
    id:int
    name:str
    email:str

    class Config:
        orm_mode = True