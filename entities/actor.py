from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Para lectura (responses)
class Actor(BaseModel):
    actor_id: int
    first_name: str
    last_name: str
    last_update: datetime

# Para creación (POST)
class ActorCreate(BaseModel):
    first_name: str
    last_name: str

# Para actualización (PUT)
class ActorUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
