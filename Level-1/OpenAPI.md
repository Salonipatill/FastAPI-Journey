OpenAPI in FastAPI — Interview Questions and Answers

1. What is OpenAPI in FastAPI?
OpenAPI is a standard specification used by FastAPI to describe an API's endpoints, parameters, request bodies, and responses. FastAPI automatically generates OpenAPI documentation.

2. Why do we use OpenAPI in FastAPI?
OpenAPI helps developers understand, test, and integrate APIs without needing to read the internal implementation.

3. How does FastAPI generate OpenAPI documentation?
FastAPI uses route definitions, Python type hints, and Pydantic models to automatically generate an OpenAPI schema.

4. What is the OpenAPI schema?
The OpenAPI schema is a structured document, usually in JSON format, that describes an API's endpoints, input parameters, request bodies, responses, and other details.

5. What is Swagger UI in FastAPI?
Swagger UI is an interactive API documentation interface that allows developers to view and test API endpoints directly in a browser. In FastAPI, it is available at /docs by default.

6. What is ReDoc in FastAPI?
ReDoc is another interface for viewing API documentation. FastAPI provides it by default at /redoc.

7. What is the difference between OpenAPI and Swagger UI?
- OpenAPI: The specification that describes the API.
- Swagger UI: A tool that displays the OpenAPI specification as interactive documentation.

8. What is the default URL for OpenAPI in FastAPI?
The default OpenAPI schema URL is /openapi.json.

FastAPI's default documentation URLs are:
- /docs — Swagger UI
- /redoc — ReDoc
- /openapi.json — OpenAPI schema

9. Can we customize OpenAPI documentation in FastAPI?
Yes. We can customize the API title, description, version, tags, and other metadata when creating the FastAPI application.
from fastapi import FastAPIapp = FastAPI(    title="Student API",    description="API for managing student data",    version="1.0.0")


10. Can we disable OpenAPI documentation in FastAPI?
Yes. We can disable the schema and documentation interfaces by setting their URLs to None.
app = FastAPI(    docs_url=None,    redoc_url=None,    openapi_url=None)



This disables the automatic OpenAPI schema endpoint and its default documentation interfaces.

Quick revision
Term	Meaning
OpenAPI	Standard specification describing an API
OpenAPI schema	Structured API description
Swagger UI	Interactive API testing and documentation
ReDoc	API documentation interface
/openapi.json	Default OpenAPI schema endpoint

Interview tip: Remember the difference between the specification (OpenAPI), the schema (the actual API description), and the interface (Swagger UI or ReDoc).