from pydantic import BaseModel
from typing import Optional


class StudentInput(BaseModel):
    name: str
    age: int
    department: str
    email: str
    phone: Optional[str] = None


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    department: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None


class StudentResponse(BaseModel):
    id: str
    name: str
    age: int
    department: str
    email: str
    phone: Optional[str] = None
    createdAt: str