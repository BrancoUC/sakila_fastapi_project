# routers/payment_router.py
from fastapi import APIRouter, HTTPException
from typing import List
from entities.payment import Payment, PaymentCreate
from controllers.payment_controller import PaymentController

router = APIRouter()
controller = PaymentController()

@router.get("/", response_model=List[Payment])
def get_all_payments():
    return controller.list_payments()

@router.get("/{payment_id}", response_model=Payment)
def get_payment(payment_id: int):
    result = controller.get_payment(payment_id)
    if not result:
        raise HTTPException(status_code=404, detail="Payment not found")
    return result

@router.post("/", response_model=bool)
def create_payment(data: PaymentCreate):
    return controller.add_payment(data)

@router.put("/{payment_id}", response_model=bool)
def update_payment(payment_id: int, data: PaymentCreate):
    return controller.modify_payment(payment_id, data)

@router.delete("/{payment_id}", response_model=bool)
def delete_payment(payment_id: int):
    return controller.remove_payment(payment_id)
