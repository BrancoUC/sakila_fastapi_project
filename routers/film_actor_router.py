from fastapi import APIRouter, HTTPException
from typing import List
from entities.film_actor import FilmActor
from controllers.film_actor_controller import FilmActorController

router = APIRouter(
    prefix="/film_actor",
    tags=["film_actor"]
)

controller = FilmActorController()

@router.get("/", response_model=List[FilmActor])
def list_film_actors():
    result = controller.list_film_actors()
    return result

@router.get("/{film_id}/{actor_id}", response_model=FilmActor)
def get_film_actor(film_id: int, actor_id: int):
    result = controller.get_film_actor(film_id, actor_id)
    if not result:
        raise HTTPException(status_code=404, detail="FilmActor not found")
    return result

@router.post("/", response_model=bool)
def add_film_actor(film_actor: FilmActor):
    success = controller.add_film_actor(film_actor.dict())
    if not success:
        raise HTTPException(status_code=500, detail="Error adding FilmActor")
    return True

@router.put("/{film_id}/{actor_id}", response_model=bool)
def modify_film_actor(film_id: int, actor_id: int, film_actor: FilmActor):
    success = controller.modify_film_actor(film_id, actor_id, film_actor.dict())
    if not success:
        raise HTTPException(status_code=500, detail="Error modifying FilmActor")
    return True

@router.delete("/{film_id}/{actor_id}", response_model=bool)
def remove_film_actor(film_id: int, actor_id: int):
    success = controller.remove_film_actor(film_id, actor_id)
    if not success:
        raise HTTPException(status_code=500, detail="Error deleting FilmActor")
    return True
