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

def get_user_by_id(db:Session,id:int):
    return db.query(models.User).get(id)

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def update_user(db:Session,user_id:int,user:schemas.UserRegister):
    db_item=get_user_by_id(db,user_id)
    updated_user=user.dict()

    for key,value in updated_user.items():
        if value!=None:
            setattr(db_item,key,value)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_user(db:Session,user_id:int):
    db.query(models.User).filter(models.User.id==user_id).delete()
    db.commit()
    return {'msg':'deleted succesfully'}