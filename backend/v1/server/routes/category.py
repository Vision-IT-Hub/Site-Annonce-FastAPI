from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session

from ..jwt_decode import JWTBearer
from ..settings.database_settngs import get_db
from ..serializers.category import CreateCategory
from ..queries_database.queries_categories import create_category, get_all_categroy, destroy
from ..models.category import ResponseModel


router = APIRouter()


# ---------------------[CATEGORY]------------------------------

@router.post(
    "/category/create/",
    response_description="category data added into the queries_database",
    dependencies=[Depends(JWTBearer())],
    responses={401: {"response": Depends(JWTBearer())}},
)
async def create_category_data(category: CreateCategory = Body(...), db: Session = Depends(get_db)):
    new_category = await create_category(category, db)
    return ResponseModel(new_category, "category added successfully.")


@router.get(
    '/category/all/get',
    response_description="Get All Categories",
    dependencies=[Depends(JWTBearer())],
    responses={401: {"response": Depends(JWTBearer())}},
)
async def all_category(db: Session = Depends(get_db)):
    return await get_all_categroy(db)


@router.delete(
    "/category/delete/{id}",
    response_description="Category data deleted from the queries_database",
    dependencies=[Depends(JWTBearer())],
    responses={401: {"response": Depends(JWTBearer())}},
)
async def destroy(id: int, db: Session = Depends(get_db)):
    return destroy(id, db)
