from fastapi import APIRouter, status, HTTPException, Header, Depends

router = APIRouter()


@router.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
