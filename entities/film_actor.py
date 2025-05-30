from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FilmActor(BaseModel):
    actor_id: int
    film_id: int
    last_update: Optional[datetime] = None