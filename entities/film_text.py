from pydantic import BaseModel

class FilmText(BaseModel):
    film_id: int
    title: str
