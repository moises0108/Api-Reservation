#Python
from datetime import datetime

#SQLAlchemy
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table
#app_reservation
from .database import Base

service_workers_table = Table(
    "association",
    Base.metadata,
    Column("services_id", ForeignKey("services.id"),primary_key=True),
    Column("workers_id", ForeignKey("workers.id"),primary_key=True),
)

workers_disponibility_table = Table(
    "association",
    Base.metadata,
    Column("disponibility_id", ForeignKey("disponibility.id"),primary_key=True),
    Column("workers_id", ForeignKey("workers.id"),primary_key=True),
)


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

    service = relationship("Service", back_populates="user")

class Service(Base):
    __tablename__="services"

    id = Column(Integer,primary_key=True,index=True)
    name_service = Column(String)

    users_id=Column(Integer,ForeignKey("users.id"))
    users = relationship("User", back_populates="services")
    workers= relationship("workers",secondary=service_workers_table)

class Worker(Base):
    __tablename__="workers"

    id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String)
    last_name = Column(String)

    
    disponibility= relationship("Disponibility",back_populates="Worker")

class Disponibility(Base):
    __tablename__="disponibility"

    id = Column(Integer,primary_key=True,index=True)
    date_disponible = Column(DateTime)
    hour_disponible = Column(Integer)

    workers=relationship("Worker",back_populates="disponibility")
