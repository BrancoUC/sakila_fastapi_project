from pydantic import BaseModel
from typing import Optional, List


class FilmBase(BaseModel):
    title: str
    description: Optional[str] = None
    release_year: Optional[int] = None
    language_id: int
    original_language_id: Optional[int] = None
    rental_duration: int
    rental_rate: float
    length: Optional[int] = None
    replacement_cost: float
    rating: Optional[str] = "G"
    special_features: Optional[List[str]] = []

class FilmCreate(FilmBase):
    pass

class Film(FilmBase):
    film_id: int

    class Config:
        orm_mode = True
