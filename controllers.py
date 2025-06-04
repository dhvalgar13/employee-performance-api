from fastapi import APIRouter, HTTPException
from services import EmployeeService
from schemas import *

router = APIRouter()
service = EmployeeService()

@router.post("/employees", response_model=EmployeeOut)
def create_employee(emp: EmployeeCreate):
    return service.add_employee(emp.name, emp.department)

@router.get("/employees", response_model=List[EmployeeOut])
def list_employees():
    return service.list_employees()

@router.get("/employees/{emp_id}", response_model=EmployeeOut)
def get_employee(emp_id: str):
    emp = service.get_employee(emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@router.post("/employees/{emp_id}/reviews", response_model=ReviewOut)
def add_review(emp_id: str, review: ReviewCreate):
    rev = service.add_review(emp_id, review.reviewer, review.score, review.feedback)
    if not rev:
        raise HTTPException(status_code=404, detail="Employee not found")
    return rev

@router.get("/employees/top-performers", response_model=List[EmployeeOut])
def top_performers():
    return service.get_top_performers()
