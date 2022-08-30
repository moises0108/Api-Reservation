#SQLAlchemy
from sqlalchemy.orm import Session

#Api_reservation
from . import models,schemas

def create_user(db:Session,user:schemas.UserRegister):
    db_user=models.User(**user)
    db.add(db_user)
    db.commit
    db.refresh
    return {'msg':'Created Succesfully'}