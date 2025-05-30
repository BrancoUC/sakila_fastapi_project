from fastapi import APIRouter, HTTPException
from controllers.address_controller import AddressController
from entities.address import Address, AddressCreate
from typing import List

router = APIRouter()

@router.get("/addresses", response_model=List[Address])
def list_addresses():
    controller = AddressController()
    result = controller.list_addresses()
    controller.close()
    return result

@router.get("/addresses/{address_id}", response_model=Address)
def get_address(address_id: int):
    controller = AddressController()
    result = controller.get_address(address_id)
    controller.close()
    if not result:
        raise HTTPException(status_code=404, detail="Address not found")
    return result

@router.post("/addresses")
def create_address(address: AddressCreate):
    controller = AddressController()
    controller.add_address(address.dict())
    controller.close()
    return {"message": "Address created successfully"}

@router.put("/addresses/{address_id}")
def update_address(address_id: int, address: AddressCreate):
    controller = AddressController()
    if not controller.get_address(address_id):
        controller.close()
        raise HTTPException(status_code=404, detail="Address not found")
    controller.modify_address(address_id, address.dict())
    controller.close()
    return {"message": "Address updated successfully"}

@router.delete("/addresses/{address_id}")
def delete_address(address_id: int):
    controller = AddressController()
    if not controller.get_address(address_id):
        controller.close()
        raise HTTPException(status_code=404, detail="Address not found")
    controller.remove_address(address_id)
    controller.close()
    return {"message": "Address deleted successfully"}
