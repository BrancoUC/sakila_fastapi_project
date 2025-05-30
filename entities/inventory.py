# entities/inventory.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Inventory(BaseModel):
    inventory_id: int
    film_id: int
    store_id: int
    last_update: Optional[datetime] = None

    class Config:
        orm_mode = True
