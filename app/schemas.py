from pydantic import BaseModel, EmailStr
from typing import List, Optional

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

# User Schemas
class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str

class UserCreate(UserBase):
    password: str

    
class LoginCreate(BaseModel):
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None

class UserInDBBase(UserBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic V2

class User(UserInDBBase):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str

# Post Schemas
class PostBase(BaseModel):
    title: Optional[str] = None
    text: str

class PostCreate(BaseModel):
    title: str
    text: str

class PostUpdate(BaseModel):
    title: Optional[str] = None
    text: Optional[str] = None

class PostInDBBase(PostBase):
    id: int
    author_id: int

    class Config:
        from_attributes = True  # Pydantic V2

class Post(PostInDBBase):
    pass
 