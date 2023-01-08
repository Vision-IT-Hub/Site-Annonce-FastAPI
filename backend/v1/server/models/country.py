from typing import List
from datetime import datetime
from pydantic import BaseModel, Field
from bson import ObjectId


# Country Model
class Country(BaseModel):
    country_name: str
    slug: str = Field(None, )
    created_at: datetime = datetime.now()
    _id: ObjectId

    class Config:
        schema_extra = {
            "example": {
                "country_name": "CI",
                "_id": "63bae696c0d9592d443de860",
            }
        }


# City Model
class City(BaseModel):
    country: List[Country]
    city_name: str
    slug: str
    created_at: datetime = datetime.now()
    _id: ObjectId

    class Config:
        schema_extra = {
            "example": {
                "country": "[CI]",
                "city_name": "CI",
                "create_at": "2019-04-01T00:00:00.000Z",
                "_id": "1",
            }
        }


# Sector Model
class Sector(BaseModel):
    city: List[City]
    sector_name: str
    sector_description: str
    slug: str
    created_at: datetime = datetime.now()
    _id: ObjectId

    class Config:
        schema_extra = {
            "example": {
                "city": "[Abj]",
                "sector_name": "Poy",
                "sector_description": "Show",
                "slug": "",
                "create_at": "2019-04-01T00:00:00.000Z",
                "_id": "1",
            }
        }

    def __str__(self):
        return self.sector_name


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
