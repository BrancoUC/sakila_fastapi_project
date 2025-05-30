from fastapi import APIRouter, HTTPException
from entities.city import City, CityCreate
from controllers.city_controller import CityController
from typing import List

router = APIRouter()

@router.get("/", response_model=List[City])
def list_cities():
    controller = CityController()
    cities = controller.list_cities()
    controller.close()
    return cities

@router.get("/{city_id}", response_model=City)
def get_city(city_id: int):
    controller = CityController()
    city = controller.get_city(city_id)
    controller.close()
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city

@router.post("/")
def create_city(city: CityCreate):
    controller = CityController()
    controller.add_city(city.dict())
    controller.close()
    return {"message": "City created successfully"}

@router.put("/{city_id}")
def update_city(city_id: int, city: CityCreate):
    controller = CityController()
    if not controller.get_city(city_id):
        controller.close()
        raise HTTPException(status_code=404, detail="City not found")
    controller.modify_city(city_id, city.dict())
    controller.close()
    return {"message": "City updated successfully"}

@router.delete("/{city_id}")
def delete_city(city_id: int):
    controller = CityController()
    if not controller.get_city(city_id):
        controller.close()
        raise HTTPException(status_code=404, detail="City not found")
    controller.remove_city(city_id)
    controller.close()
    return {"message": "City deleted successfully"}
