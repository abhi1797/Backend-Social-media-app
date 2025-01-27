from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional
from typing_extensions import Annotated


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

#entry by the user
class PostCreate(PostBase):
    pass

#sending response back to the web/user
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime


class UserLogin(BaseModel):
    email: EmailStr
    password: str

#sending response back to the web
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

class PostOut(BaseModel):
    Post: Post
    votes: int   

#entry by the user
class UserCreate(BaseModel):
    email : EmailStr
    password: str





class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]= None

class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(strict=True, ge=0, le=1)]




