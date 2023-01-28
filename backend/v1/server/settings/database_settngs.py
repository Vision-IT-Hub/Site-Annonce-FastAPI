import motor.motor_asyncio
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .secret_configs import get_secret

Base = declarative_base()


def get_db_mongo(url="mongodb://localhost:27017", collection=""):
    client = motor.motor_asyncio.AsyncIOMotorClient(url)
    database = client.VIH
    return database.get_collection(collection)


url = get_secret('URL_POSTGRES')
engine = create_engine(url)


async def get_db():
    SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()
