from pydantic import BaseModel, EmailStr, constr
from typing import List, Optional

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: constr(min_length=8)

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

class PostBase(BaseModel):
    text: constr(max_length=1048576)  # 1 MB limit

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True