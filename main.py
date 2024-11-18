from http.client import HTTPException
from fastapi import FastAPI,Depends,APIRouter
from database import Base, engine,  SessionLocal
from typing import List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import Users


Base.metadata.create_all(bind=engine)

app = FastAPI()
api_router = APIRouter(prefix="/api")

def get_db():
    db = SessionLocal()
    try:
        yield db
    
    finally:
        db.close()

@api_router.get("/hello/")
async def data():
    return{"message":"Namastey"}
app.include_router(api_router)

class UserSchema(BaseModel): 
    name: str
    email: str
    password: str 
    
class UserCreateSchema(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        from_attribute = True

@api_router.get("/users/", response_model=List[UserCreateSchema])
async def get_users(db: Session = Depends(get_db)):
    try:
        return db.query(Users).order_by(Users.id).all()
    except:
        return HTTPException(status_code=500, detail="Something went wrong")
   
@api_router.post("/users/create/",response_model=UserCreateSchema)
async def create_users(users: UserSchema, db: Session = Depends(get_db)):
    try:
        u = Users(name=users.name, email=users.email, password=users.password)
        db.add(u)
        db.commit()
        db.refresh(u) 
        return u 
        
    except:
        return HTTPException(status_code=400, detail="Invalid Request")


@api_router.put("/users/{users_id}",response_model=UserSchema)
async def Update_users(users_id:int,users: UserSchema, db: Session = Depends(get_db)):
    try:
        u=db.query(Users).filter(Users.id==users_id).first()
        u.name=users.name
        u.email=users.email
        db.add(u)
        db.commit()        
        return u
    except:
        return HTTPException(status_code=404, detail="User not found")

@api_router.delete("/users/{users_id}")
async def delete_users(users_id: int, db: Session = Depends(get_db)):
    try:
        u = db.query(Users).filter(Users.id == users_id).first()
        
        if u is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        db.delete(u)
        db.commit()
        
        return {"message": f"User with id {users_id} has been deleted"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while deleting the user")
app.include_router(api_router)