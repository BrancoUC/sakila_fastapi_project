from fastapi import APIRouter, HTTPException
from typing import List
from entities.inventory import Inventory
from controllers.inventory_controller import InventoryController

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"]
)

controller = InventoryController()

@router.get("/", response_model=List[Inventory])
def list_inventories():
    return controller.list_inventories()

@router.get("/{inventory_id}", response_model=Inventory)
def get_inventory(inventory_id: int):
    inventory = controller.get_inventory(inventory_id)
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return inventory

@router.post("/", response_model=bool)
def add_inventory(inventory: Inventory):
    success = controller.add_inventory(inventory.dict())
    if not success:
        raise HTTPException(status_code=500, detail="Error adding inventory")
    return True

@router.put("/{inventory_id}", response_model=bool)
def modify_inventory(inventory_id: int, inventory: Inventory):
    success = controller.modify_inventory(inventory_id, inventory.dict())
    if not success:
        raise HTTPException(status_code=500, detail="Error modifying inventory")
    return True

@router.delete("/{inventory_id}", response_model=bool)
def remove_inventory(inventory_id: int):
    success = controller.remove_inventory(inventory_id)
    if not success:
        raise HTTPException(status_code=500, detail="Error deleting inventory")
    return True
