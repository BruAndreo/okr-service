from fastapi import APIRouter, status
from okr.resources.schemas.objectives import NewObjective

router = APIRouter(
    prefix="/objectives",
    tags=["objectives"],
    responses={404: {"error": "Not Found"}}
)

@router.post("/", summary="Create objetive", status_code=status.HTTP_201_CREATED)
def create_objective(new_objetive: NewObjective):
    print(new_objetive.dict())
    return { "objective_id": 1 }

@router.get("/", summary="Get Objectives")
def get_all_objectives():
    return {"Hello": "World"}