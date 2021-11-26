from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Authentication", "Auth"],
    responses={404: {"error": "Not Found"}}
)

@router.post("/")
async def auth():
    return { "token": "abc-123" }