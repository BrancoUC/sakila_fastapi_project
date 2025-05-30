from fastapi import APIRouter, HTTPException
from entities.category import Category
from controllers.category_controller import CategoryController
from typing import List

router = APIRouter()

@router.get("/categories", response_model=List[Category])
def list_categories():
    controller = CategoryController()
    result = controller.list_categories()
    controller.close()
    return result

@router.get("/categories/{category_id}", response_model=Category)
def get_category(category_id: int):
    controller = CategoryController()
    category = controller.get_category(category_id)
    controller.close()
    if not category:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return category

@router.post("/categories")
def create_category(category: Category):
    controller = CategoryController()
    controller.add_category(category.dict())
    controller.close()
    return {"message": "Categoría creada correctamente"}

@router.put("/categories/{category_id}")
def update_category(category_id: int, category: Category):
    controller = CategoryController()
    if not controller.get_category(category_id):
        controller.close()
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    controller.modify_category(category_id, category.dict())
    controller.close()
    return {"message": "Categoría actualizada correctamente"}

@router.delete("/categories/{category_id}")
def delete_category(category_id: int):
    controller = CategoryController()
    if not controller.get_category(category_id):
        controller.close()
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    controller.remove_category(category_id)
    controller.close()
    return {"message": "Categoría eliminada correctamente"}
