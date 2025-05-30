# routers/language_router.py
from fastapi import APIRouter, HTTPException
from controllers.language_controller import LanguageController
from entities.language import Language, LanguageCreate

router = APIRouter()
controller = LanguageController()


@router.get("/", response_model=list[Language])
def get_languages():
    return controller.list_languages()


@router.get("/{language_id}", response_model=Language)
def get_language(language_id: int):
    language = controller.get_language(language_id)
    if not language:
        raise HTTPException(status_code=404, detail="Language not found")
    return language


@router.post("/", response_model=bool)
def create_language(language: LanguageCreate):
    return controller.add_language(language.dict())


@router.put("/{language_id}", response_model=bool)
def update_language(language_id: int, language: LanguageCreate):
    if not controller.get_language(language_id):
        raise HTTPException(status_code=404, detail="Language not found")
    return controller.modify_language(language_id, language.dict())


@router.delete("/{language_id}", response_model=bool)
def delete_language(language_id: int):
    if not controller.get_language(language_id):
        raise HTTPException(status_code=404, detail="Language not found")
    return controller.remove_language(language_id)
