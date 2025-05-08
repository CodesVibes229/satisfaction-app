from pydantic import BaseModel
from typing import Optional, List

class ResponseCreate(BaseModel):
    answer: str

class ResponseOut(BaseModel):
    id: int
    answer: str

    class Config:
        orm_mode = True

class SurveyCreate(BaseModel):
    title: str
    description: Optional[str] = None

class SurveyOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    responses: List[ResponseOut] = []

    class Config:
        orm_mode = True
