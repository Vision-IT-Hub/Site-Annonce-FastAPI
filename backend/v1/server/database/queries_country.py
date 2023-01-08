from ..serializers.country import country_serializer
from .database_settngs import country_collection
from bson.objectid import ObjectId


# Create a new country into to the database
async def create_country(country_data: dict) -> dict:
    country_data["slug"] = "-".join(country_data["country_name"].split(' ')).lower()
    country = await country_collection.insert_one(country_data)
    new_country = await country_collection.find_one({"_id": country.inserted_id})
    return country_serializer(new_country)


# Delete a country from the database
async def delete_country(id: str):
    country = await country_collection.find_one({"_id": ObjectId(id)})
    print(country)
    if country:
        await country_collection.delete_one({"_id": ObjectId(id)})
        return True


# Update a country with a matching ID
async def update_country(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    country = await country_collection.find_one({"_id": ObjectId(id)})
    if country:
        updated_country = await country_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_country:
            return True
        return False


# Get all country present in the database
async def get_all_country():
    countries = []
    async for country in country_collection.find():
        countries.append(country_serializer(country))
    return countries


# Get a student with a matching ID
async def get_country_by_id(id: str) -> dict:
    country = await country_collection.find_one({"_id": ObjectId(id)})
    if country:
        return country_serializer(country)
