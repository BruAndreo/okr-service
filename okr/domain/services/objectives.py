from okr.domain.repositories.objective_repository import ObjectiveRepository
from okr.resources.schemas.objectives import NewObjective
from okr.domain.models.objectives import Objectives as ObjectivesModel
from okr.utils.uuid import uuid_generator

class Objectives:
    
    def create_new_objetive(self, objective: NewObjective, creator: str):
        new_objective = ObjectivesModel(objective_id=uuid_generator(), 
                                        user_id=creator, 
                                        **objective.dict())

        repo = ObjectiveRepository()
        repo.insert_one(new_objective.dict())
        return new_objective.objective_id