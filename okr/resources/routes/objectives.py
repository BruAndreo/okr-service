from fastapi import APIRouter, status, Depends, Request
from okr.resources.middlewares.authentication import AuthenticationMiddleware
from okr.resources.schemas.objectives import NewObjective
from okr.domain.services.objectives import Objectives

router = APIRouter(
    prefix="/objectives",
    tags=["objectives"],
    responses={404: {"error": "Not Found"}},
    dependencies=[Depends(AuthenticationMiddleware())]
)

@router.post("/", summary="Create objetive", status_code=status.HTTP_201_CREATED)
def create_objective(new_objetive: NewObjective, request: Request):
    objectives_service = Objectives()
    objective_id = objectives_service.create_new_objetive(objective=new_objetive, creator=request.state.token["user_id"])
    return { "objective_id": objective_id }

@router.get("/", summary="Get Objectives")
def get_all_objectives():
    return {"Hello": "World"}