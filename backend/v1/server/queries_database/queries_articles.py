from bson.objectid import ObjectId

from ..serializers.articles import ArticleSerializer
from ..settings.database_settngs import get_db_mongo


article_collection = get_db_mongo(collection="articles")


# Create a new articles into to the queries_database
async def create_article(article_data: dict) -> dict:
    article_data["slug"] = "-".join(article_data["article_name"].split(' ')).lower()
    article = await article_collection.insert_one(article_data)
    new_article = await article_collection.find_one({"_id": article.inserted_id})
    return ArticleSerializer(new_article)


# Delete a articles from the queries_database
async def delete_article(id: str):
    article = await article_collection.find_one({"_id": ObjectId(id)})
    if article:
        await article_collection.delete_one({"_id": ObjectId(id)})
        return True


# Update a articles with a matching ID
# TODO: Il faut verifier le id entrant
async def update_article(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    article = await article_collection.find_one({"_id": ObjectId(id)})
    if article:
        updated_article = await article_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_article:
            return True
        return False


# Get all articles present in the queries_database
async def get_all_articles():
    articles = []
    async for article in article_collection.find():
        articles.append(ArticleSerializer(article))
    return articles


# TODO: Il faut verifier le id entrant
# Get a student with a matching ID
async def get_article_by_id(id: str) -> dict:
    article = await article_collection.find_one({"_id": ObjectId(id)})
    if article:
        return ArticleSerializer(article)
    return {}
