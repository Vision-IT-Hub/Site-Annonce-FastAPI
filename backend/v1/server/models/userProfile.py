import datetime

from sqlalchemy import Integer, String, DateTime, UniqueConstraint, Boolean
from sqlalchemy.sql.schema import Column
from sqlalchemy_utils import EmailType

from ..settings.database_settngs import Base


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(EmailType, unique=True)
    password = Column(String, nullable=False)
    verified = Column(Boolean, default=False)
    photo = Column(String, nullable=True)
    role = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    __table_args__ = (UniqueConstraint('username', 'email', name='username_email_uc'),
                      )

    class Config:
        schema_extra = {
            "example": {
                "first_name": "jean",
                "last_name": "max",
                "username": "jm",
                "email": "jm@mail.ru",
                "password": "********",
                "passwordConfirm": "********",
                "verified": True,
                "photo": "./photo1",
                "role": "user",
                "created_at": "2019-04-01T00:00:00.000Z",
                "updated_at": "2019-04-01T00:00:00.000Z",
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
