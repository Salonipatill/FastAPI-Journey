# FastAPI Architecture

FastAPI architecture **describes how a request travels from the client to the backend**, gets processed, and returns a response.

## Request–Response Flow

1. **Client:** The frontend or application that sends a request.
2. **HTTP Request:** The client sends a request to access or modify data.
3. **Uvicorn (ASGI Server):** Receives the request and passes it to the FastAPI application.
4. **FastAPI:** Processes the request and matches it to the correct route.
5. **Router/Endpoint:** Identifies which function should handle the request.
6. **Business Logic:** Applies the application's rules and processes the data.
7. **Database/External API:** Stores or retrieves data, or communicates with another service.
8. **Response:** FastAPI returns the result, commonly in JSON format, to the client.

## Example: Fetching User Details

Suppose a React frontend needs to fetch user details for user ID 10.

**Request flow:**

`React Frontend → HTTP GET Request → Uvicorn → FastAPI → User Route → Database`

**Response flow:**

`Database → FastAPI → JSON Response → React Frontend`

Example request:

```http
GET /users/10
```

Example JSON response:

```json
{
  "id": 10,
  "name": "Saloni"
}
```

## How to Speak in an Interview

"FastAPI follows a request–response architecture. First, the client sends an HTTP request. Uvicorn, which is an ASGI server, receives the request and passes it to FastAPI. FastAPI matches the request with the appropriate route. The endpoint executes the business logic and interacts with the database or an external API if required. Finally, FastAPI returns a response, usually in JSON format, to the client."

