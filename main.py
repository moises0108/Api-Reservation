from fastapi import FastAPI
from fastapi import status,Depends,HTTPException,Body,Path
#SqlAlchemy
from sqlalchemy.orm import Session
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

@app.post(
    path="/register",
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
    )
def create_user(db:Session=Depends(get_db),user:schemas.UserRegister=Body(...)):
    """
    Signup

    this path operation register a user in the app

    Parameters:
    - Request Body Parameter
        - user:UserRegister
    
    Returns a Json with a msg if the operation is succesfully:
    
    """
    if crud.get_user_by_email(db,user.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Email already exists")

    return crud.create_user(db,user)
