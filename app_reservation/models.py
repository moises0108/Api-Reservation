#Python
from datetime import datetime

#SQLAlchemy
from sqlalchemy import Boolean, Column, ForeignKey, Integer,Date, String,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table
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
    birth_date=Column(Date)
    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime,default=datetime.now())

    user_service = relationship("UserService", back_populates="users")

class UserService(Base):
    __tablename__="users_services"
    id = Column(Integer,primary_key=True,index=True)

    users_id=Column(Integer,ForeignKey("users.id"))
    users = relationship("User", back_populates="user_service")

    services_id=Column(Integer,ForeignKey("services.id"))
    services = relationship("Service", back_populates="user_service")


class Service(Base):
    __tablename__="services"

    id = Column(Integer,primary_key=True,index=True)
    name_service = Column(String)

    user_service = relationship("UserService", back_populates="services")
    services_workers = relationship("ServiceWorker", back_populates="services")


class ServiceWorker(Base):
    __tablename__="services_workers"
    id = Column(Integer,primary_key=True,index=True)

    services_id=Column(Integer,ForeignKey("services.id"))
    services = relationship("Service", back_populates="services_workers")

    workers_id=Column(Integer,ForeignKey("workers.id"))
    workers = relationship("Worker", back_populates="services_workers")


class Worker(Base):
    __tablename__="workers"

    id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String)
    last_name = Column(String)

    
    services_workers = relationship("ServiceWorker", back_populates="workers")
    workers_disponibility = relationship("WorkerDisponibility", back_populates="workers")


class WorkerDisponibility(Base):
    __tablename__="workers_disponibility"
    id = Column(Integer,primary_key=True,index=True)

    workers_id=Column(Integer,ForeignKey("workers.id"))
    workers = relationship("Worker", back_populates="workers_disponibility")

    disponibility_id=Column(Integer,ForeignKey("disponibility.id"))
    disponibility = relationship("Disponibility", back_populates="workers_disponibility")

class Disponibility(Base):
    __tablename__="disponibility"

    id = Column(Integer,primary_key=True,index=True)
    date_disponible = Column(DateTime,unique=True)
    hour_disponible = Column(Integer,unique=True)

    workers_disponibility = relationship("WorkerDisponibility", back_populates="disponibility")
