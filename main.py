from fastapi import FastAPI
#app reservation
from app_reservation import crud, models, schemas
from app_reservation.database import SessionLocal, engine


app=FastAPI()


models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()