## Testing in FastAPI
## 1. Pytest

Pytest is a Python framework used to write and run tests.

def test_add():
    assert 2 + 3 == 5

Interview:

Pytest is a Python testing framework used to test application code.

## 2. TestClient

TestClient is used to test FastAPI endpoints without running the actual server.

from fastapi.testclient import TestClient

client = TestClient(app)

response = client.get("/users")

Interview:

TestClient allows us to send HTTP requests to FastAPI endpoints during testing.

Pytest
  ↓
runs the test
  ↓
TestClient
  ↓
calls your FastAPI endpoint
  ↓
assert
  ↓
checks the result



learn TestClient in FastAPI, follow these steps in order.

Step 1 — Install dependencies
pip install pytest httpx
Step 2 — Create your FastAPI app

main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}
Step 3 — Create a test file

Create:

test_main.py
Step 4 — Import TestClient
from fastapi.testclient import TestClient
from main import app
Step 5 — Create the client
client = TestClient(app)

Think:

TestClient = a fake client that can send requests to your FastAPI app.

Step 6 — Write your test
def test_home():
    response = client.get("/")

    assert response.status_code == 200

You can also check the response data:

def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
Step 7 — Run the test

From the project folder:

pytest -v

## 3. Unit Testing

Tests one small part of the application independently.

Example:

calculate_total()
      ↓
    Test

Interview:

Unit testing tests individual functions or components.

## 4. API Testing

Tests whether an API endpoint works correctly.

Example:

response = client.get("/users")

assert response.status_code == 200

Interview:

API testing checks whether API endpoints return the expected response.

## 5. Integration Testing

Tests whether multiple components work together.

Example:

API → Service → Database
 ↑
Test

Interview:

Integration testing checks the interaction between multiple components.

## 6. Mocking

Mocking means replacing a real dependency with a fake one during testing.

Example:

Real API → expensive/slow ❌

Mock API → fake response ✅

If your application calls an external AI API, you can mock it instead of actually calling the AI service.

Interview:

Mocking replaces real dependencies with fake ones during testing.

## 7. Async Testing

Used to test asynchronous functions using async/await.

async def test_user():
    result = await get_user()
    assert result is not None

Interview:

Async testing is used to test asynchronous code and functions.