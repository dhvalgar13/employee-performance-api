from typing import List
from uuid import uuid4
from datetime import datetime

class Employee:
    def __init__(self, name: str, department: str):
        self.id = str(uuid4())
        self.name = name
        self.department = department
        self.reviews: List[PerformanceReview] = []

class PerformanceReview:
    def __init__(self, reviewer: str, score: float, feedback: str):
        self.id = str(uuid4())
        self.reviewer = reviewer
        self.score = score
        self.feedback = feedback
        self.created_at = datetime.utcnow()
