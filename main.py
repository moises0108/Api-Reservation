#Python
from typing import List
#FastApi
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

# Path Operation

## Users

### Register a User
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

### Show a User
@app.get(
    path="/user/{user_id}",
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"],
    response_model=schemas.User
)
def show_user(
    db:Session=Depends(get_db),
    user_id:int=Path(
        ...,
        title="User id",
        description="Id of the User you want",
        example=1
        ),
    ):
    """
    Show User

    this path operation Show a select user in the app

    Parameters:
    - Path Parameter
        - user_id:int
    
    Returns a Json with the basic user information:
    - first_name: str
    - last_name: str
    - email: EmailStr
    - contact_number:str
    - birth_date:date
    """
    user=crud.get_user_by_id(db,user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user

###Show all users
@app.get(
    path='/users',
    status_code=status.HTTP_200_OK,
    summary='Show all users',
    tags=["Users"],
    response_model=List[schemas.User]
)
def show_all_users(
    db:Session=Depends(get_db)
    ):
    return crud.get_users(db)
###Delete a User
@app.delete(
    path="/users/{user_id}/delete",
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
    )
def delete_a_user(
    user_id:int=Path(
        ...,
        gt=0,
        title="user id",
        description="id of the user you want delete",
        example=2
    ),
    db:Session=Depends(get_db)
):
    """
    Delete a User

    this path operation delete a user in the app

    Parameters:
    - Request Path Parameter
        - user_id
    
    Returns a Json with the message user delete succesfull if it work:
    """
    return crud.delete_user(db=db,user_id=user_id)
###Update a User
@app.put(
    path="/users/{user_id}/update",
    response_model=schemas.User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["Users"]
    )
def update_a_user(
    db:Session=Depends(get_db),
    user_id:int=Path(
        ...,
        gt=0,
        title="user_id",
        description="id of the user you want update"
        ),
    user:schemas.UserRegister=Body(...)
    ):
    """
    Update a User

    this path operation update a user in the app

    Parameters:
    - Request Path Parameter:
        - user_id
    Request Body Parameter:
        -user:UpdateUser
    Returns a Json with basic user information of the user updated:
    - email:EmailStr
    - first_name:str
    - last_name:str
    - birth_date:date
    """
    return crud.update_user(db,user_id,user)

##Service

###Create a Service
@app.post(
    path="/service/create",
    status_code=status.HTTP_201_CREATED,
    summary="Create a Service",
    tags=["Service"]
)
def create_a_service(
    db:Session=Depends(get_db),
    service:schemas.Service=Body(...)
    ):
    """
    Create a Service

    this path operation create a service in the app

    Parameters:
    - Request Body Parameter
        - service:Service
    
    Returns a Json with a msg if the operation is succesfully:
    """
    return crud.create_service(db,service)


###Show a Service
@app.get(
    path="/service/{id_service}",
    status_code=status.HTTP_200_OK,
    summary='Get a Service',
    response_model=schemas.Service
)
def get_service(
    db:Session=Depends(get_db),
    id_service:int=Path(
        ...,
        title="Service id",
        description="Id of the Service you want",
        example=1,
        )
    ):
    """
    Show a Service

    this path operation Show a select server in the app

    Parameters:
    - Path Parameter
        - id_service:int
    
    Returns a Json with the basic service information:
    - name_service: str
    """
    return crud.get_service(db,id_service)
