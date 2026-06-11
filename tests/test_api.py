from fastapi.testclient import TestClient

from src import app

client = TestClient(app.app)


def test_root_redirects_to_index():
    response = client.get("/")

    assert response.status_code == 200
    assert str(response.url).endswith("/static/index.html")


def test_get_activities_returns_all_activities():
    response = client.get("/activities")

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "Chess Club" in response.json()


def test_signup_for_activity_adds_participant():
    activity_name = "Math Club"
    new_email = "teststudent@mergington.edu"

    response = client.post(f"/activities/{activity_name}/signup", params={"email": new_email})

    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {new_email} for {activity_name}"}
    assert new_email in app.activities[activity_name]["participants"]


def test_signup_duplicate_returns_400():
    activity_name = "Chess Club"
    existing_email = "michael@mergington.edu"

    response = client.post(f"/activities/{activity_name}/signup", params={"email": existing_email})

    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"


def test_signup_unknown_activity_returns_404():
    response = client.post("/activities/Unknown%20Club/signup", params={"email": "teststudent@mergington.edu"})

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_from_activity_removes_participant():
    activity_name = "Gym Class"
    existing_email = "john@mergington.edu"

    response = client.delete(f"/activities/{activity_name}/participants", params={"email": existing_email})

    assert response.status_code == 200
    assert response.json() == {"message": f"Removed {existing_email} from {activity_name}"}
    assert existing_email not in app.activities[activity_name]["participants"]


def test_unregister_nonexistent_participant_returns_404():
    activity_name = "Drama Club"
    missing_email = "newstudent@mergington.edu"

    response = client.delete(f"/activities/{activity_name}/participants", params={"email": missing_email})

    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"


def test_unregister_unknown_activity_returns_404():
    response = client.delete("/activities/Unknown%20Club/participants", params={"email": "teststudent@mergington.edu"})

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
