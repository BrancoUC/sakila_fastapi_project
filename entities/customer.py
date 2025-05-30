from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Customer(BaseModel):
    customer_id: int
    store_id: int
    first_name: str
    last_name: str
    email: Optional[str]
    address_id: int
    active: int
    create_date: datetime
    last_update: Optional[datetime]


class CustomerCreate(BaseModel):
    store_id: int
    first_name: str
    last_name: str
    email: Optional[str]
    address_id: int
    active: Optional[int] = 1


class CustomerUpdate(CustomerCreate):
    pass
