from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from pydantic import BaseModel
from app.schemas import UserCreate, UserResponse
from app.services.user_service import create_user, authenticate_user

router = APIRouter()

# Schema for login request body
class LoginRequest(BaseModel):
    email: str
    password: str


@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

# @router.post("/login")
# def login(email: str, password: str, db: Session = Depends(get_db)):
#     return {"access_token": authenticate_user(db, email, password)}
@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    return {"access_token": authenticate_user(db, request.email, request.password)}