import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.VIH

country_collection = database.get_collection("country")
articles_collection = database.get_collection("articles")
orders_collection = database.get_collection("orders")

