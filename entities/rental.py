from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RentalBase(BaseModel):
    rental_date: datetime
    inventory_id: int
    customer_id: int
    return_date: Optional[datetime] = None
    staff_id: int

class RentalCreate(RentalBase):
    pass

class Rental(RentalBase):
    rental_id: int
    last_update: datetime

    class Config:
        from_attributes = True
