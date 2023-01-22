from typing import List, Optional
from pydantic import BaseModel, Field


class ItemCategory(BaseModel):
    id : int
    category_name : str
    description : str
    slug : str 

    class Config:
        orm_mode=True 

class CreateCategory(BaseModel):
    category_name : str
    description : str
    