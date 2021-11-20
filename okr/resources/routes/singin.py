from fastapi import APIRouter, status
from okr.data.db import db
from okr.resources.models.user import User

router = APIRouter(
    prefix="/singin",
    tags=["sing-in"],
    responses={404: {"error": "Not Found"}}
)

@router.post("/", summary="Sing in", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):

    ret = db.users.insert_one(user.dict())

    if ret.inserted_id is not None:
        return {"user_id": user.user_id}
    return {"error": "Error to sing in"}