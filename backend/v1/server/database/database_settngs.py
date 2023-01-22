import motor.motor_asyncio
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

def get_db_mongo(url="mongodb://localhost:27017", collection=""):
    client = motor.motor_asyncio.AsyncIOMotorClient(url)
    database = client.VIH
    return database.get_collection(collection)
"""
url="postgresql://postgres:tito2010@localhost/site_annonce"
engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
base = declarative_base()
"""

async def get_db():
    url = "postgresql://postgres:tito2010@localhost/site_annonce"
    engine = create_engine(url)
    SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    db = SessionLocal()
    try:
        yield  db
    except:
        db.close()

