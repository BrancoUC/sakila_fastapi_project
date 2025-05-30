from fastapi import APIRouter, HTTPException
from controllers.actor_controller import ActorController
from entities.actor import Actor, ActorCreate, ActorUpdate
from typing import List

router = APIRouter()

@router.get("/", response_model=List[Actor])
def list_actors():
    controller = ActorController()
    actors = controller.list_actors()
    controller.close()
    return actors

@router.get("/{actor_id}", response_model=Actor)
def get_actor(actor_id: int):
    controller = ActorController()
    actor = controller.get_actor(actor_id)
    controller.close()
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor

@router.post("/actors")
def create_actor(actor: ActorCreate):  
    controller = ActorController()
    controller.add_actor(actor.dict())
    controller.close()
    return {"message": "Actor created successfully"}

@router.put("/actors/{actor_id}")
def update_actor(actor_id: int, actor: ActorUpdate):
    controller = ActorController()
    if not controller.get_actor(actor_id):
        controller.close()
        raise HTTPException(status_code=404, detail="Actor not found")
    controller.modify_actor(actor_id, actor.dict(exclude_unset=True))
    controller.close()
    return {"message": "Actor updated successfully"}

@router.delete("/{actor_id}")
def delete_actor(actor_id: int):
    controller = ActorController()
    if not controller.get_actor(actor_id):
        controller.close()
        raise HTTPException(status_code=404, detail="Actor not found")
    controller.remove_actor(actor_id)
    controller.close()
    return {"message": "Actor deleted successfully"}