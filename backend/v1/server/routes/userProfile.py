from fastapi import APIRouter, Body, HTTPException, Depends, status, Response
from sqlalchemy.orm import Session

from ..jwt_decode import signJWT, JWTBearer
from ..settings import utils
from ..settings.database_settngs import get_db
from ..queries_database.queries_userProfile import create_user, get_all_user_data
from ..models.userProfile import ResponseModel, User
from ..serializers.userProfile import CreateUserSchema, LoginUserSchema


router = APIRouter()


@router.post(
    "/user/create/",
    response_description="user data added into the queries_database",
)
async def create_user_data(user: CreateUserSchema = Body(...), db: Session = Depends(get_db)):
    new_user = await create_user(user, db)
    return ResponseModel(new_user, "user created successfully.")


@router.post('/user/login/')
async def login_user(
        request: LoginUserSchema,
        db: Session = Depends(get_db),
):
    email = request.email.lower()
    password = request.password
    qs_by_email = db.query(User).filter(User.email == email).first()

    if not qs_by_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Incorrect Email or Password')

    if not utils.verify_password(password, qs_by_email.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Incorrect Email or Password')
    # Create access token
    access_token = signJWT(qs_by_email.id)
    # Send both access
    return ResponseModel(access_token, 'access_token')


@router.get('/user/logout/', status_code=status.HTTP_200_OK, dependencies=[Depends(JWTBearer())])
def logout(response: Response):
    response.set_cookie('logged_in', '', -1)

    return ResponseModel("success", '')


@router.get('/user/all/get', response_description="Get All users",
            dependencies=[Depends(JWTBearer())],
            responses={401: {"response": Depends(JWTBearer())}},
            )
async def get_all_user(db: Session = Depends(get_db)):
    return await get_all_user_data(db)
