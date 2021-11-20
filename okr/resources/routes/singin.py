from fastapi import APIRouter, status
from okr.resources.schemas.user import UserBody
from okr.domain.user import User

router = APIRouter(
    prefix="/singin",
    tags=["sing-in"],
    responses={404: {"error": "Not Found"}}
)

@router.post("/", summary="Sing in", status_code=status.HTTP_201_CREATED)
async def create_user(user_body: UserBody):
    user= User()
    user_id = user.create_user(user_body.dict())

    return {"user_id": user_id}
