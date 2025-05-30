from fastapi import APIRouter, HTTPException
from controllers.customer_controller import CustomerController
from entities.customer import Customer, CustomerCreate, CustomerUpdate
from typing import List

router = APIRouter()


@router.get("/", response_model=List[Customer])
def list_customers():
    controller = CustomerController()
    customers = controller.list_customers()
    controller.close()
    return customers


@router.get("/{customer_id}", response_model=Customer)
def get_customer(customer_id: int):
    controller = CustomerController()
    customer = controller.get_customer(customer_id)
    controller.close()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


@router.post("/")
def create_customer(customer: CustomerCreate):
    controller = CustomerController()
    controller.add_customer(customer.dict())
    controller.close()
    return {"message": "Customer created successfully"}


@router.put("/{customer_id}")
def update_customer(customer_id: int, customer: CustomerUpdate):
    controller = CustomerController()
    if not controller.get_customer(customer_id):
        controller.close()
        raise HTTPException(status_code=404, detail="Customer not found")
    controller.modify_customer(customer_id, customer.dict())
    controller.close()
    return {"message": "Customer updated successfully"}


@router.delete("/{customer_id}")
def delete_customer(customer_id: int):
    controller = CustomerController()
    if not controller.get_customer(customer_id):
        controller.close()
        raise HTTPException(status_code=404, detail="Customer not found")
    controller.remove_customer(customer_id)
    controller.close()
    return {"message": "Customer deleted successfully"}
