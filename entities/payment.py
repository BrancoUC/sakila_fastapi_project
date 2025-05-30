# entities/payment.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Payment(BaseModel):
    payment_id: int
    customer_id: int
    staff_id: int
    rental_id: Optional[int]
    amount: float
    payment_date: datetime
    last_update: Optional[datetime]

class PaymentCreate(BaseModel):
    customer_id: int
    staff_id: int
    rental_id: Optional[int]
    amount: float
