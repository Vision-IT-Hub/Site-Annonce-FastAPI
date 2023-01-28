from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column
from ..settings.database_settngs import Base


class Category(Base):
    __tablename__ = 'category'

    category_name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    slug = Column(String, nullable=False)
    id = Column(Integer, primary_key=True, index=True)

    class Config:
        schema_extra = {
            "example": {
                "category_name": "Immobilier",
                "description": "ok",
                "slug": "immobilier",
                "id": 1
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
