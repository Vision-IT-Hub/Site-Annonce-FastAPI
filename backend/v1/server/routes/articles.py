from fastapi import APIRouter, Body, HTTPException, Depends
from fastapi.encoders import jsonable_encoder

from ..jwt_decode import JWTBearer
from ..queries_database.queries_articles import (
    create_article,
    update_article,
    delete_article,
    get_all_articles,
    get_article_by_id
)
from ..models.articles import Articles, ResponseModel, ErrorResponseModel

router = APIRouter()


@router.post(
    "/article/create/",
    response_description="article data added into the queries_database",
    dependencies=[Depends(JWTBearer())],
    responses={401: {"response": Depends(JWTBearer())}}
)
async def create_article_data(article: Articles = Body(...)):
    article = jsonable_encoder(article)
    new_article = await create_article(article)
    return ResponseModel(new_article, "article added successfully.")


@router.delete(
    "/article/delete/{id}",
    response_description="article data deleted from the queries_database",
    dependencies=[Depends(JWTBearer())],
    responses={401: {"response": Depends(JWTBearer())}}
)
async def delete_article_data(id: str):
    deleted_article = await delete_article(id)
    if deleted_article:
        return ResponseModel(
            "article with ID: {} removed".format(id), "article deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "article with id {0} doesn't exist".format(id)
    )


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
