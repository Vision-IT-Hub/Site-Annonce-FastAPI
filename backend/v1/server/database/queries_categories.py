from ..serializers.category import ItemCategory , CreateCategory
from fastapi import Depends
from sqlalchemy.orm import Session
from .database_settngs import get_db
from ..models.category import Category
from fastapi import HTTPException, status


async def create_category(request:CreateCategory, db: Session = Depends(get_db))-> ItemCategory:
    slug =  "-".join(request.category_name.split(' ')).lower()
    new_category = Category(category_name=request.category_name, description=request.description, slug=slug )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

async def destroy(id: int, db: Session):
    category = db.query(Category).filter(Category.id == id)
    if not category.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Category with id {id} not found")

    category.delete(synchronize_session=False)
    db.commit()
    return "done"


async def get_all_categroy(db: Session):
    category =  db.query(Category).all()
    return category 