#Python
from datetime import date
from typing import Optional
from xmlrpc.client import DateTime
#Pydantic
from pydantic import BaseModel,validator
from pydantic import Field,EmailStr
#SqlModel
from sqlmodel import SQLModel

class Person(BaseModel):
    first_name:str=Field(
        ...,
        title="First Name",
        description="First Name of the user",
        min_length=1,
        max_length=100,
        example="Moises")

    last_name:str=Field(
        ...,
        title="Last Name",
        description="Last Name of the user",
        min_length=1,
        max_length=100,
        example="Patino"
        )

    class Config:
        orm_mode=True


class User(Person):
    email:EmailStr=Field(
        ...,
        example="user@gmail.com"
        )
    

    contact_number:str=Field(
        ...,
        title="Phone Number",
        description="Phone number of the user",
        min_length=1,
        max_length=100,
        example="+584140436425"
        )
    birth_date:date=Field(
        ...,
        title='Birth Date',
        description='Birth Date',
        example="2000-08-01",
    )

class UserRegister(User):
    hash_password:str=Field(
        ...,
        title="Password",
        description="Password of the user",
        min_length=8,
        max_length=16,
        example="Moises123")

class Service(BaseModel):
    name_service:str=Field(
        ...,
        title="Service Name",
        description="Service Name",
        min_length=1,
        max_length=100)
    class Config:
        orm_mode=True
class Worker(Person):
    pass


class Disponibility(BaseModel):
    date_disponible:date=Field(
        ...,
        title="date disponible",
        example="2023-08-01"
        )
    hour_disponible:int=Field(
        ...,
        lt=10,
        title="hour disponible",
        description="hour that you want to schedule",
        )
    @validator('date_disponible')
    def date_valid(cls,date_disponible:date):
        today_date=date.today()
        if date_disponible<today_date:
            raise ValueError("You cannot schedule a date that has already passed")
        return date_disponible
    class Config:
        orm_mode=True
    
class TwoModels(BaseModel):
    id_left:int=Field(...)
    id_right:int=Field(...)
    class Config:
        orm_mode=True

class UserService(TwoModels):
    pass

class ServiceWorker(TwoModels):
    pass

class WorkerDisponibility(TwoModels):
    pass

#SqlModel
class UpdateUser(SQLModel):
    first_name:Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=50,
        example="Moises"
        )
    last_name:Optional[str]= Field(
        default=None,
        min_length=1,
        max_length=50,
        example="Patino"
        )
    email:Optional[EmailStr] = Field(
        default=None,
        example="moisespatinoh@gmail.com"
    )
    birth_date : Optional[date] = Field(default=None,example="2000-08-01")
    hash_password:Optional[str] = Field(
        default=None,
        min_length=8,
        max_length=16,
        example="Moises123"
        )
    contact_number:Optional[str]= Field(
        default=None,
        min_length=1,
        max_length=50,
        example="+584140436425"
        )