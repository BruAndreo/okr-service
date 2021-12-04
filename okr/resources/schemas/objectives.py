from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NewObjective(BaseModel):
    # objective_id: str
    # user_id: str
    title: str
    description: str
    # percentage: float
    start_date: Optional[datetime] = datetime.now()
    finish_date: Optional[datetime]
    # created_at: datetime
    # updated_at: datetime