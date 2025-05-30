from fastapi import APIRouter, HTTPException
from controllers.country_controller import CountryController
from entities.country import Country, CountryCreate, CountryUpdate
from typing import List

router = APIRouter()


@router.get("/", response_model=List[Country])
def list_countries():
    controller = CountryController()
    countries = controller.list_countries()
    controller.close()
    return countries


@router.get("/{country_id}", response_model=Country)
def get_country(country_id: int):
    controller = CountryController()
    country = controller.get_country(country_id)
    controller.close()
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")
    return country


@router.post("/")
def create_country(country: CountryCreate):
    controller = CountryController()
    controller.add_country(country.dict())
    controller.close()
    return {"message": "Country created successfully"}


@router.put("/{country_id}")
def update_country(country_id: int, country: CountryUpdate):
    controller = CountryController()
    if not controller.get_country(country_id):
        controller.close()
        raise HTTPException(status_code=404, detail="Country not found")
    controller.modify_country(country_id, country.dict())
    controller.close()
    return {"message": "Country updated successfully"}


@router.delete("/{country_id}")
def delete_country(country_id: int):
    controller = CountryController()
    if not controller.get_country(country_id):
        controller.close()
        raise HTTPException(status_code=404, detail="Country not found")
    controller.remove_country(country_id)
    controller.close()
    return {"message": "Country deleted successfully"}
