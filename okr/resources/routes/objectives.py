from fastapi import APIRouter

router = APIRouter(
    prefix="/objectives",
    tags=["objectives"],
    responses={404: {"error": "Not Found"}}
)

@router.get("/", summary="Get Objectives")
def get_all_objectives():
    return {"Hello": "World"}