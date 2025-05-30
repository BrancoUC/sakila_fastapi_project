from fastapi import APIRouter, HTTPException
from controllers.film_controller import FilmController
from entities.film import Film, FilmCreate
from typing import List

router = APIRouter()
controller = FilmController()

@router.get("/", response_model=List[Film])
def list_films():
    return controller.list_films()

@router.get("/{film_id}", response_model=Film)
def get_film(film_id: int):
    film = controller.get_film(film_id)
    if not film:
        raise HTTPException(status_code=404, detail="Film no encontrado")
    return film

@router.post("/", status_code=201)
def create_film(film: FilmCreate):
    controller.add_film(film.dict())
    return {"message": "Film creado correctamente"}

@router.put("/{film_id}")
def update_film(film_id: int, film: FilmCreate):
    controller.modify_film(film_id, film.dict())
    return {"message": "Film actualizado correctamente"}

@router.delete("/{film_id}")
def delete_film(film_id: int):
    controller.remove_film(film_id)
    return {"message": "Film eliminado correctamente"}
