from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class StoreBase(BaseModel):
    manager_staff_id: int
    address_id: int
    last_update: Optional[datetime] = None

class StoreCreate(StoreBase):
    pass

class Store(StoreBase):
    store_id: int

    class Config:
        from_attributes = True  # para pydantic v2
