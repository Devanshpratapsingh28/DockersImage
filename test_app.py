from app import app


def test_home():
    response = app.test_client().get("/")
    # assert is used to verify the expected outcome
    assert response.status_code == 200 # Check if the response status code is 200 (OK)
    assert response.get_data(as_text=True) == "<h1>Hello World!</h1>" # Check if the response data matches the expected output
