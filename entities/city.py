from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class City(BaseModel):
    city_id: int
    city: str
    country_id: int
    last_update: datetime

class CityCreate(BaseModel):
    city: str
    country_id: int
