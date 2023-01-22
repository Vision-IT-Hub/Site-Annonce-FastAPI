from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from ..database.database_settngs import get_db
from ..serializers.category import ItemCategory, CreateCategory
from fastapi import Depends

from ..database.queries_categories import create_category, get_all_categroy, destroy

from ..models.category import (Category, ErrorResponseModel, ResponseModel)

router = APIRouter()


# ---------------------[COUNTRY]------------------------------

@router.post("/category/create/", response_description="category data added into the database")
async def create_category_data(category: CreateCategory = Body(...), db: Session = Depends(get_db)):
    new_category = await create_category(category, db)
    return ResponseModel(new_category , "category added successfully.")

@router.get('/category/all/get', response_description="Get All Categories")
async def all_category(db: Session = Depends(get_db)):
    return await get_all_categroy(db)

@router.delete("/category/delete/{id}", response_description="Category data deleted from the database")
async def destroy(id: int, db: Session = Depends(get_db)):
    return destroy(id, db)


