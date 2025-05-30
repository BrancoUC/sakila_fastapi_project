from fastapi import APIRouter, HTTPException
from typing import List
from entities.film_category import FilmCategory
from controllers.film_category_controller import FilmCategoryController

router = APIRouter(
    prefix="/film_category",
    tags=["film_category"]
)

controller = FilmCategoryController()

@router.get("/", response_model=List[FilmCategory])
def list_film_categories():
    return controller.list_film_categories()

@router.get("/{film_id}/{category_id}", response_model=FilmCategory)
def get_film_category(film_id: int, category_id: int):
    film_category = controller.get_film_category(film_id, category_id)
    if not film_category:
        raise HTTPException(status_code=404, detail="FilmCategory not found")
    return film_category

@router.post("/", response_model=bool)
def add_film_category(film_category: FilmCategory):
    success = controller.add_film_category(film_category.dict())
    if not success:
        raise HTTPException(status_code=500, detail="Error adding FilmCategory")
    return True

@router.delete("/{film_id}/{category_id}", response_model=bool)
def remove_film_category(film_id: int, category_id: int):
    success = controller.remove_film_category(film_id, category_id)
    if not success:
        raise HTTPException(status_code=500, detail="Error deleting FilmCategory")
    return True
