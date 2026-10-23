## Request Body in FastAPI

A **request body** is the part of an HTTP request that carries data from the client to the server. It is commonly used with `POST`, `PUT`, and `PATCH` requests to send data in JSON format.

**Example:**

```http
POST /users
Content-Type: application/json

{
    "name": "Saloni",
    "age": 21
}
```

**Explanation:**
- `POST /users`: Sends a request to create a new user.
- `Content-Type: application/json`: Specifies that the request body contains JSON data.
- **Request body:** Contains the user's name and age.

**How to speak:**

"A request body carries data from the client to the server. In FastAPI, we commonly use it to send JSON data when creating or updating resources. FastAPI validates the incoming data using Pydantic models."