from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class StaffBase(BaseModel):
    first_name: str
    last_name: str
    address_id: int
    email: Optional[EmailStr] = None
    store_id: int
    active: bool
    username: str
    password: Optional[str] = None  # normalmente no se devuelve la contraseña

class StaffCreate(StaffBase):
    password: str  # requerido al crear

class Staff(StaffBase):
    staff_id: int
    last_update: datetime

    class Config:
        from_attributes = True
