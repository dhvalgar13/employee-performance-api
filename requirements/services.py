from models import Employee, PerformanceReview
from typing import Dict, List

class EmployeeService:
    def __init__(self):
        self.employees: Dict[str, Employee] = {}

    def add_employee(self, name: str, department: str) -> Employee:
        emp = Employee(name, department)
        self.employees[emp.id] = emp
        return emp

    def get_employee(self, emp_id: str) -> Employee:
        return self.employees.get(emp_id)

    def delete_employee(self, emp_id: str):
        return self.employees.pop(emp_id, None)

    def list_employees(self) -> List[Employee]:
        return list(self.employees.values())

    def add_review(self, emp_id: str, reviewer: str, score: float, feedback: str) -> PerformanceReview:
        emp = self.get_employee(emp_id)
        if not emp:
            return None
        review = PerformanceReview(reviewer, score, feedback)
        emp.reviews.append(review)
        return review

    def get_top_performers(self, min_score=4.5) -> List[Employee]:
        return [e for e in self.employees.values() if any(r.score >= min_score for r in e.reviews)]
