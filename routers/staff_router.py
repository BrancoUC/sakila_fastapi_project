from fastapi import APIRouter, HTTPException
from entities.staff import Staff, StaffCreate
from controllers.staff_controller import StaffController

router = APIRouter()
controller = StaffController()

@router.get("/", response_model=list[Staff])
def get_all_staff():
    staff_list = controller.list_staff()
    return staff_list

@router.get("/{staff_id}", response_model=Staff)
def get_staff(staff_id: int):
    staff = controller.get_staff(staff_id)
    if staff is None:
        raise HTTPException(status_code=404, detail="Staff member not found")
    return staff

@router.post("/", response_model=dict)
def create_staff(staff: StaffCreate):
    success = controller.add_staff(staff.dict())
    if not success:
        raise HTTPException(status_code=500, detail="Failed to create staff member")
    return {"message": "Staff member created successfully"}

@router.put("/{staff_id}", response_model=dict)
def update_staff(staff_id: int, staff: StaffCreate):
    success = controller.modify_staff(staff_id, staff.dict())
    if not success:
        raise HTTPException(status_code=500, detail="Failed to update staff member")
    return {"message": "Staff member updated successfully"}

@router.delete("/{staff_id}", response_model=dict)
def delete_staff(staff_id: int):
    success = controller.remove_staff(staff_id)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to delete staff member")
    return {"message": "Staff member deleted successfully"}
