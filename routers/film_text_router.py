from fastapi import APIRouter, HTTPException
from typing import List
from entities.film_text import FilmText
from controllers.film_text_controller import FilmTextController

router = APIRouter(
    prefix="/film_text",
    tags=["film_text"]
)

controller = FilmTextController()

@router.get("/", response_model=List[FilmText])
def list_film_texts():
    return controller.list_film_texts()

@router.get("/{film_id}", response_model=FilmText)
def get_film_text(film_id: int):
    film_text = controller.get_film_text(film_id)
    if not film_text:
        raise HTTPException(status_code=404, detail="FilmText not found")
    return film_text

@router.post("/", response_model=bool)
def add_film_text(film_text: FilmText):
    success = controller.add_film_text(film_text.dict())
    if not success:
        raise HTTPException(status_code=500, detail="Error adding FilmText")
    return True

@router.put("/{film_id}", response_model=bool)
def modify_film_text(film_id: int, film_text: FilmText):
    success = controller.modify_film_text(film_id, film_text.dict())
    if not success:
        raise HTTPException(status_code=500, detail="Error modifying FilmText")
    return True

@router.delete("/{film_id}", response_model=bool)
def remove_film_text(film_id: int):
    success = controller.remove_film_text(film_id)
    if not success:
        raise HTTPException(status_code=500, detail="Error deleting FilmText")
    return True
