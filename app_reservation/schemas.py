#Python
from datetime import date
from typing import Optional
from xmlrpc.client import DateTime
#Pydantic
from pydantic import BaseModel
from pydantic import Field,EmailStr


class Person(BaseModel):
    first_name:str=Field(
        ...,
        title="First Name",
        description="First Name of the user",
        min_length=1,
        max_length=100)

    last_name:str=Field(
        ...,
        title="Last Name",
        description="Last Name of the user",
        min_length=1,
        max_length=100)


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
        max_length=100)


class Service(BaseModel):
    service_name:str=Field(
        ...,
        title="Service Name",
        description="Service Name",
        min_length=1,
        max_length=100)

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
        description="hour that you want to agend",
        )