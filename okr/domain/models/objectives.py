from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Objectives(BaseModel):
    objective_id: str
    user_id: str
    title: str
    description: str
    percentage: float = 0.0
    start_date: Optional[datetime] = datetime.now()
    finish_date: Optional[datetime]
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()