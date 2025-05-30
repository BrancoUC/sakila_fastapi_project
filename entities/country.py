from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Country(BaseModel):
    country_id: int
    country: str
    last_update: datetime


class CountryCreate(BaseModel):
    country: str


class CountryUpdate(CountryCreate):
    pass
