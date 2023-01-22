from fastapi_contrib.serializers.common import Serializer
from fastapi_contrib.serializers import openapi
from ..models.articles import (Articles, Review)

def ArticleSerializer(article):
   data_ = {
             k: article[k] for k in Articles.schema()["required"]
           }
   data_["_id"] = str(article["_id"])

   return data_
