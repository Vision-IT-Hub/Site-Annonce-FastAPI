import bson
from bson.objectid import ObjectId

from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..settings.database_settngs import get_db
from ..queries_database.get_user_by_id import get_user
from ..jwt_decode import JWTBearer, decodeJWT
from ..queries_database.queries_articles import (
    create_article,
    update_article,
    delete_article,
    get_all_articles,
    get_article_by_id
)
from ..models.articles import Articles, ResponseModel, ErrorResponseModel, CreateArticles

router = APIRouter()


def dep(db: Session = Depends(get_db)):
    db = db
    return db


@router.post(
    "/article/create/",
    response_description="article data added into the queries_database",
    dependencies=[Depends(JWTBearer())],
    responses={401: {"response": Depends(JWTBearer())}}
)
async def create_article_data(token: str = Depends(JWTBearer()), article: CreateArticles = Body()):
    user = get_user(decodeJWT(token)["user_id"])
    article = jsonable_encoder(article)
    article["user"] = user
    new_article = await create_article(article)

    return ResponseModel(new_article, "article added successfully.")


@router.delete(
    "/article/delete/{id}",
    response_description="article data deleted from the queries_database",
    dependencies=[Depends(JWTBearer())],
    responses={401: {"response": Depends(JWTBearer())}}
)
async def delete_article_data(id: str = ObjectId(), token: str = Depends(JWTBearer())):
    current_user_id = decodeJWT(token)["user_id"]
    try:
        article = await get_article_by_id(id)
        if article:
            user_id_created_article = article["user"][0]["id"]

            if current_user_id == user_id_created_article:
                deleted_article = await delete_article(id)
                if deleted_article:
                    return ResponseModel(
                        "article with ID: {} removed".format(id), "article deleted successfully"
                    )
                raise HTTPException(status_code=404, detail=" ID Article Not Found")
            raise HTTPException(status_code=401, detail="Unauthorized access")
        raise HTTPException(status_code=404, detail=" ID Article Not Found")
    except bson.errors.InvalidId:
        raise HTTPException(status_code=404, detail="ID Article Not Found")


@router.put(
    "/article/update/{id}",
    dependencies=[Depends(JWTBearer())],
    responses={401: {"response": Depends(JWTBearer())}}
)
async def update_article_data(id: str, req: Articles = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_article = await update_article(id, req)
    if updated_article:
        return ResponseModel(
            "article with ID: {} name update is successful".format(id),
            "article name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the article data.",
    )


@router.get(
    "/article/all/get/",
    response_description="Get All articles",
    dependencies=[Depends(JWTBearer())],
    responses={401: {"response": Depends(JWTBearer())}}
)
async def get_all_article_data():
    articles = await get_all_articles()
    if articles:
        return ResponseModel(articles, "articles data retrieved successfully")
    return ResponseModel(articles, "Empty list returned")


@router.get(
    "/article/get/{id}",
    response_description="article data retrieved",
    dependencies=[Depends(JWTBearer())],
    responses={401: {"response": Depends(JWTBearer())}}
)
async def get_article_by_id_data(id):
    try:
        article = await get_article_by_id(id)
        if article:
            return ResponseModel(article, "article data retrieved successfully")
        return ErrorResponseModel("An error occurred.", 404, "article doesn't exist.")

    except HTTPException:
        raise HTTPException(status_code=401, detail="Unauthorized access")
