#Python
from datetime import date
from typing import Optional
#Pydantic
from pydantic import BaseModel
from pydantic import Field,EmailStr

class User(BaseModel):
    email:EmailStr=Field(
        ...,
        example="user@gmail.com"
        )
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

