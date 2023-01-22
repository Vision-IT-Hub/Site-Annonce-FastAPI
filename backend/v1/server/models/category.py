from sqlalchemy import Integer, String, Column
from sqlalchemy.sql.schema import Column
from pydantic import BaseModel, Field
from ..database.database_settngs import Base
from uuid import uuid4

class Category(Base):
    __tablename__ = 'category'
    
    category_name = Column(String, nullable=False) 
    description  = Column(String, nullable=True) 
    slug = Column(String, nullable=False)
    id = Column(Integer, primary_key=True, index=True) 
    
    class Config:
        schema_extra = {
            "example": {
                "category_name":"Immobilier",
                "description":"ok",
                "slug":"immobilier",
                "id":1
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
