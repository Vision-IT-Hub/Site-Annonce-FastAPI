from datetime import datetime

from fastapi import Depends
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..jwt_decode import decodeJWT
from ..settings import utils
from ..settings.database_settngs import get_db
from ..models.userProfile import User
from ..serializers.userProfile import CreateUserSchema


async def create_user(request: CreateUserSchema, db: Session = Depends(get_db())):
    email = request.email.lower()
    qs_email = db.query(User).filter(User.email == email)
    if qs_email.first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='Account already exist')
    # Compare password and passwordConfirm
    request.password = utils.hash_password(request.password)
    del request.passwordConfirm
    request.verified = True
    request.created_at = datetime.utcnow()
    request.updated_at = request.created_at
    new_user = User(
        first_name=request.first_name,
        last_name=request.last_name,
        username=request.username,
        email=request.email.lower(),
        password=request.password,
        verified=request.verified,
        photo=request.photo,
        role=request.role,
        created_at=request.created_at,
        updated_at=request.updated_at
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def get_all_user_data(db: Session = Depends(get_db())):
    users = db.query(User).all()
    return users


async def get_current_user_by_token(token: str, db: Session = Depends(get_db())):
    tk = decodeJWT(token)
    qs_id = db.query(User).filter(User.id == tk['user_id'])
    return qs_id
