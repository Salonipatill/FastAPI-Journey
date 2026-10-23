# FastAPI

## 1. What is FastAPI?

FastAPI is a modern, high-performance Python web framework used to build APIs and backend applications.[Done]

## FastAPI is built on 

the Starlette framework for core web functionality and the Pydantic library for data validation, parsing, and serialization using Python type hints.

*Serialization is the process of converting an object into a format such as JSON or bytes so that it can be stored or transmitted. Deserialization is the reverse process, which converts the data back into an object.*

**Core web functionality refers to the fundamental operations required to receive, process, and respond to client requests in a web application.**

In Starlette, core web functionality includes:
- HTTP Request/Response Handling: Receiving HTTP requests and returning responses.
- Routing: Mapping incoming requests to the appropriate endpoint.
- Middleware: Processing requests and responses through intermediate components.
- WebSocket Support: Enabling real-time, bidirectional communication.
- Background Tasks: Executing tasks after sending a response.

**A WebSocket is a communication protocol that allows a client and a server to exchange data in real time through a persistent, two-way connection.**

### B. Pydantic → Data Validation

Pydantic validates and parses data based on defined types and rules.

### C. Python Type Hints → Type Information

Python type hints define the expected data types of function parameters and return values.

FastAPI uses them for request validation, response handling, and automatic API documentation.

## 3. Uses of FastAPI

- REST API development
- Microservices
- Backend applications
- AI and LLM integration
- Machine learning APIs

**Quick Summary:**
- **FastAPI:** Builds APIs.
- **Starlette:** Handles web functionality.
- **Pydantic:** Validates data.
- **Type Hints:** Define expected data types.