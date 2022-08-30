#SQLAlchemy
from sqlalchemy.orm import Session

#Api_reservation
from . import models,schemas

def create_user(db:Session,user:schemas.UserRegister):
    db_user=models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {'msg':'Created Succesfully'}

def get_user_by_email(db:Session,email:str):
    return db.query(models.User).filter(models.User.email==email).first()