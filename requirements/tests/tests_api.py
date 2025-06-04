from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_employee_and_review():
    # Create employee
    resp = client.post("/employees", json={"name": "Alice", "department": "Finance"})
    assert resp.status_code == 200
    emp = resp.json()
    emp_id = emp["id"]

    # Add review
    review = {
        "reviewer": "Bob",
        "score": 4.8,
        "feedback": "Excellent performance"
    }
    r_resp = client.post(f"/employees/{emp_id}/reviews", json=review)
    assert r_resp.status_code == 200
    data = r_resp.json()
    assert data["score"] == 4.8

def test_get_top_performers():
    resp = client.get("/employees/top-performers")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
