from fastapi import APIRouter, HTTPException
from controllers.store_controller import StoreController
from entities.store import StoreCreate, Store

router = APIRouter()
store_controller = StoreController()

@router.get("/stores", response_model=list[Store])
def get_stores():
    return store_controller.list_stores()

@router.get("/stores/{store_id}", response_model=Store)
def get_store(store_id: int):
    store = store_controller.get_store(store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store

@router.post("/stores", response_model=bool)
def create_store(store_data: StoreCreate):
    success = store_controller.add_store(store_data)
    if not success:
        raise HTTPException(status_code=400, detail="Failed to add store")
    return True

@router.put("/stores/{store_id}", response_model=bool)
def update_store(store_id: int, store_data: StoreCreate):
    success = store_controller.modify_store(store_id, store_data)
    if not success:
        raise HTTPException(status_code=400, detail="Failed to update store")
    return True

@router.delete("/stores/{store_id}", response_model=bool)
def delete_store(store_id: int):
    success = store_controller.remove_store(store_id)
    if not success:
        raise HTTPException(status_code=400, detail="Failed to delete store")
    return True
