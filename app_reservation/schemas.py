#Python
from datetime import datetime
#SQLAlchemy
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship
#app_reservation
from .database import Base

class User(Base):
    __tablename__="users"
    id = Column(Integer,primary_key=True,index=True)
    email=Column(String,index=True,unique=True)
    first_name=Column(String)
    last_name=Column(String)
    contact_number=Column(String)
    hash_password=Column(String)

    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime,default=datetime.now())