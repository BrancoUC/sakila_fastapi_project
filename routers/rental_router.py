from fastapi import APIRouter, HTTPException
from entities.rental import Rental, RentalCreate
from controllers.rental_controller import RentalController

router = APIRouter()
controller = RentalController()

@router.get("/", response_model=list[Rental])
def get_all_rentals():
    rentals = controller.list_rentals()
    return rentals

@router.get("/{rental_id}", response_model=Rental)
def get_rental(rental_id: int):
    rental = controller.get_rental(rental_id)
    if rental is None:
        raise HTTPException(status_code=404, detail="Rental not found")
    return rental

@router.post("/", response_model=dict)
def create_rental(rental: RentalCreate):
    success = controller.add_rental(rental.dict())
    if not success:
        raise HTTPException(status_code=500, detail="Failed to create rental")
    return {"message": "Rental created successfully"}

@router.put("/{rental_id}", response_model=dict)
def update_rental(rental_id: int, rental: RentalCreate):
    success = controller.modify_rental(rental_id, rental.dict())
    if not success:
        raise HTTPException(status_code=500, detail="Failed to update rental")
    return {"message": "Rental updated successfully"}

@router.delete("/{rental_id}", response_model=dict)
def delete_rental(rental_id: int):
    success = controller.remove_rental(rental_id)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to delete rental")
    return {"message": "Rental deleted successfully"}
