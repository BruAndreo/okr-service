from fastapi import APIRouter
from okr.resources.schemas.auth import AuthBody
from okr.domain.services.user import User

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
    responses={404: {"error": "Not Found"}}
)

@router.post("/", summary="User Authentication")
async def auth(auth: AuthBody):
    user = User()
    auth_token = user.authenticate_user(auth)
    return { "token": auth_token }