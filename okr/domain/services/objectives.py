from okr.resources.schemas.objectives import NewObjective

class Objectives:
    
    def create_new_objetive(self, objective: NewObjective) -> int:
        print(objective.dict())
        return 1