from fastapi import APIRouter
from ..models.db import db
from ..models.user import User

router = APIRouter(
    prefix="/singin",
    tags=["sing-in"],
    responses={404: {"error": "Not Found"}}
)

@router.post("/", summary="Sing in")
async def create_user(user: User):

    ret = db.users.insert_one(user.dict())

    # print(ret.inserted_id)

    return {"user_id": ret.inserted_id}