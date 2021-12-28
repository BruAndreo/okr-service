from okr.domain.repositories.objective_repository import ObjectiveRepository
from okr.resources.schemas.objectives import NewObjective
from okr.domain.models.objectives import Objectives as ObjectivesModel

import uuid

class Objectives:
    
    def create_new_objetive(self, objective: NewObjective, creator: str):
        new_objective = ObjectivesModel(objective_id=self._generate_user_id(), 
                                        user_id=creator, 
                                        **objective.dict())

        repo = ObjectiveRepository()
        repo.insert_one(new_objective.dict())
        return new_objective.objective_id
    
    def _generate_user_id(self) -> str:
        return str(uuid.uuid4())