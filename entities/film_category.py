from pydantic import BaseModel

class FilmCategory(BaseModel):
    film_id: int
    category_id: int
