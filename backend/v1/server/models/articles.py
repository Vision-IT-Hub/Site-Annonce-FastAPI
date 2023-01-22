from typing import List
from datetime import datetime
from pydantic import BaseModel, Field
from bson import ObjectId
from enum import Enum

class Conditon(str, Enum):
   Excellent = "Excellent"
   Good = "Good"
   Fair = "Fair"

class TypeTransaction(str, Enum):
   Vente = "Vente"
   Demande = "Demande"





# Country Model
class Articles(BaseModel):
    user : List[dict] # get_user_by_id()
    article_name : str
    image : str
    brand : str
    category : List[dict] # get_category_by_id and get_list_field_category
    description : str
    rating : int
    num_reviews : int
    price : str
    count_in_stock : int
    sector : List[dict]
    phone : str
    video : str
    condition : Conditon
    article_address : str
    is_features : bool
    is_active : bool
    type_transaction : TypeTransaction
    create_at : datetime = datetime.now()
    update_at : datetime = datetime.now()
    slug: str 
    _id: ObjectId

    # TODO: faire la documentation
    class Config:
        schema_extra = {
            "example": {
                "user": [{"id":1, 
                          "lastname":"patcheko",
                          "firstname":"digbonan",
                          "email":"pa@vih.com", 
                          "email_confirmed":True,
                          "created_at":"2019-04-01T00:00:00.000Z"}],
                "article_name": "article 1",
                "image" : "1",
                "brand": 1,
                "category": [{
                    "category":{
                        "id": 1,
                        "category_name":"auto",
                        "description":"votre produit auto"
                    },
                    "champs":{
                        "marque":"mercedes",
                        "couleur":"noir",
                        "date de sortie":"2019-04-01T00:00:00.000Z"
                    }
                    
                }],
                "description": "desc 1",
                "rating":2,
                "num_reviews" : 2,
                "price": 10000,
                "count_in_stock":6,
                "sector": [
                    {   "id":1,
                        "sector_name": "Sikobois",
                        "sector_description":"magasion ablo",
                        "slug":"sikobois",
                         "created_at":"2019-04-01T00:00:00.000Z",
                        "city":{
                            "id":1,
                            "city_name":"abj",
                            "created_at":"2019-04-01T00:00:00.000Z",
                            "slug":"abj",
                            "country":{
                                "id": 1,
                                "country_name":"ci",
                                "slug":"ci",
                                "created_at":"2019-04-01T00:00:00.000Z"
                            }
                        }

                    }

                ],
                "phone":"050426587",
                "video": "1",
                "condition":"Good",
                "article_address":"chez ablo",
                "is_features":True,
                "is_active":True,
                "type_transaction":"Vente",
                "slug":"article-1"

                
            }
        }


class Review(BaseModel):
    article :  List[dict] # get_article_by_id
    name : str
    rating : int
    comment : str
    creat_at : datetime = datetime.now()
    update_at : datetime = datetime.now()

    # TODO: faire la documentation
    class Config:
        schema_extra = {
            "example": {
                
            }
        }

"""
# City Model
class City(BaseModel):
    country: List[dict]
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
"""

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
