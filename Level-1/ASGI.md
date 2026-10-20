## ASGI (Asynchronous Server Gateway Interface)

**ASGI** is a standard interface that defines how Python web applications communicate with ASGI servers.

- **FastAPI** → ASGI-compatible web framework
- **Uvicorn** → ASGI server
- **ASGI** → Communication interface between the server and application

## 1. FastAPI vs Uvicorn vs ASGI

### FastAPI → Creates the API
FastAPI is a Python web framework used to build APIs.

It provides features such as:
- Creating API routes
- Handling HTTP methods (GET, POST, PUT, DELETE)
- Request validation using Python type hints
- Response handling
- Automatic Swagger/OpenAPI documentation
- Dependency injection
- WebSocket support

### Uvicorn → Runs the API
Uvicorn is a lightweight ASGI server used to run FastAPI applications.

Its responsibilities include:
- Starting the server and listening for incoming connections
- Receiving HTTP and WebSocket requests
- Communicating with FastAPI through ASGI
- Sending responses back to clients

### ASGI → Defines the Communication
ASGI specifies how an ASGI server and a Python web application communicate.

**Compatible** means two components can work together according to a shared standard.

FastAPI is designed to work with ASGI servers such as Uvicorn because they follow the ASGI interface.

## 2. How a Request Works

**Example:** `GET /users`

1. The client sends an HTTP request to `/users`.
2. Uvicorn receives the request.
3. Uvicorn communicates with FastAPI through the ASGI interface.
4. FastAPI finds the matching `/users` route.
5. The corresponding Python function executes.
6. FastAPI prepares the response.
7. Uvicorn sends the HTTP response back to the client.

**Easy memory trick:**

- **FastAPI** = Creates and handles the API
- **Uvicorn** = Runs the server and handles network communication
- **ASGI** = Defines how the server and application communicate

## 3. Web Server

A **web server** is software that receives requests from clients and sends responses over a network.

Uvicorn acts as the web server for a FastAPI application.

## 4. Gateway

A **gateway** is a component that connects systems or controls communication between them.

It may be a separate service or application that manages the path between different systems.

**Note:** In ASGI, the word *gateway* is part of the interface's name; it does not mean that Uvicorn must be a separate API gateway service.

## 5. Message vs Event

- **Message:** The actual information being sent between components.
- **Event:** An indication that something has happened.

In ASGI, events are represented as Python dictionaries containing information about what is happening in a connection.

For example, an incoming HTTP request is represented by an ASGI event containing details such as the request method, path, and headers.