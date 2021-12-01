from typing import Dict
from fastapi.encoders import jsonable_encoder
from okr.utils.timers import Timers
from okr.config import settings

import jwt

class JWT:
    
    @staticmethod
    def generate(payload: Dict):
        return jwt.encode(
            payload=jsonable_encoder({
                **payload, 
                "exp": Timers.add_minutes_actual_time(30)
            }),
            key=settings.auth.secret,
            algorithm=settings.auth.algorithm
        )