# 🟣 Level 5 — Production & Deployment

## Testing

* Pytest
* TestClient
* Unit Testing
* API Testing
* Integration Testing
* Mocking
* Async Testing

FastAPI's testing documentation uses `TestClient` together with HTTPX and pytest.

## Docker

* Docker basics
* Dockerfile
* Docker Image
* Docker Container
* Docker Compose
* Environment Variables
* Containerized FastAPI

## Performance

* Async APIs
* Caching
* Redis
* Connection Pooling
* Rate Limiting
* Pagination
* Performance Optimization

## Production

* Logging
* Monitoring
* Health Checks
* Readiness Checks
* Error Tracking
* Security
* HTTPS
* Multiple Workers
* Restart Strategies
* Deployment Architecture

## Cloud & Deployment

* AWS
* Azure
* Google Cloud
* Cloud Run
* FastAPI Cloud
* CI/CD
* Production Deployment

FastAPI's deployment guidance covers concepts such as HTTPS, startup, restarts, replication and memory management.

### Resources

* [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/)
* [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
* [FastAPI Deployment Concepts](https://fastapi.tiangolo.com/deployment/concepts/)

---

# 🧪 Practical Projects

## Project 1 — Basic CRUD API

**Stack:**

```text
Python
FastAPI
Pydantic
```

Features:

* Create user
* Read user
* Update user
* Delete user

---

## Project 2 — FastAPI + MySQL

**Stack:**

```text
FastAPI
SQLAlchemy
MySQL
Pydantic
```

Features:

* User registration
* Login
* CRUD
* Database relationships

---

## Project 3 — Authentication API

**Stack:**

```text
FastAPI
JWT
OAuth2
MySQL
```

Features:

* Register
* Login
* JWT
* Protected routes
* Roles

---

## Project 4 — AI FastAPI Service

**Stack:**

```text
FastAPI
Python
Groq / LLM
Docker
Pytest
```

Features:

* AI endpoint
* Authentication
* Input validation
* Error handling
* Caching
* Testing
* Docker

---

# 🤖 AI + FastAPI

FastAPI is also useful for building **AI/LLM backend services**.

## Topics

* LLM API Integration
* AI Service Architecture
* Prompt Processing
* Request Validation
* Response Validation
* Groq API
* OpenAI API
* AI API Endpoints
* Authentication
* Error Handling
* Async LLM Calls
* Caching
* Rate Limiting
* Dockerized AI Services
* AI Service Deployment

### Example Architecture

```text
Frontend
   │
   ▼
FastAPI
   │
   ├── Authentication
   │
   ├── Validation
   │
   ├── Business Logic
   │
   ▼
AI Service
   │
   ▼
LLM API
   │
   ▼
Response
   │
   ▼
Frontend
```

### Project Practice

Build small services such as:

* AI Text Summarizer
* AI Chat API
* Question Answering API
* Text Classification API
* AI Recommendation API
