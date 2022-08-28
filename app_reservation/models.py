#Python
from datetime import datetime

#SQLAlchemy
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
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

    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime,default=datetime.now())

    user_service = relationship("UserService", back_populates="users_services")

class UserService(Base):
    __tablename__="users_services"
    id = Column(Integer,primary_key=True,index=True)

    users_id=Column(Integer,ForeignKey("users.id"))
    users = relationship("User", back_populates="users_services")

    services_id=Column(Integer,ForeignKey("services.id"))
    services = relationship("Service", back_populates="users_services")


class Service(Base):
    __tablename__="services"

    id = Column(Integer,primary_key=True,index=True)
    name_service = Column(String)

    user_service = relationship("UserService", back_populates="users_services")
    service_worker = relationship("ServiceWorker", back_populates="services_workers")


class ServiceWorker(Base):
    __tablename__="services_workers"
    id = Column(Integer,primary_key=True,index=True)

    services_id=Column(Integer,ForeignKey("users.id"))
    services = relationship("Service", back_populates="services_workers")

    services_id=Column(Integer,ForeignKey("workers.id"))
    workers = relationship("Worker", back_populates="services_workers")


class Worker(Base):
    __tablename__="workers"

    id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String)
    last_name = Column(String)

    
    service_worker = relationship("ServiceWorker", back_populates="services_workers")
    worker_disponibility = relationship("WorkerDisponibility", back_populates="workers_disponibility")


class WorkerDisponibility(Base):
    __tablename__="workers_disponibility"
    id = Column(Integer,primary_key=True,index=True)

    services_id=Column(Integer,ForeignKey("workers.id"))
    services = relationship("Worker", back_populates="workers_disponibility")

    services_id=Column(Integer,ForeignKey("disponibility.id"))
    disponibility = relationship("Disponibility", back_populates="workers_disponibility")

class Disponibility(Base):
    __tablename__="disponibility"

    id = Column(Integer,primary_key=True,index=True)
    date_disponible = Column(DateTime,unique=True)
    hour_disponible = Column(Integer,unique=True)

    worker_disponibility = relationship("WorkerDisponibility", back_populates="workers_disponibility")
