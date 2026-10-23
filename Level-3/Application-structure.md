# FastAPI Architecture — Interview Notes

| Topic | Interview answer |
|---|---|
| **APIRouter** | `APIRouter` is a FastAPI class used to group related API routes into separate, reusable modules. |
| **Routers** | Routers define API endpoints and connect HTTP requests to the corresponding Python functions. |
| **Modular Architecture** | Dividing a large application into separate modules for better organization, reusability, and maintainability. |
| **Services** | Services contain the business logic of the application. |
| **Schemas** | Schemas define the structure of request and response data and validate it using Pydantic. |
| **Models** | Models represent database tables and their data when using an ORM such as SQLAlchemy. |
| **Configuration** | Configuration manages application settings, such as database URLs, API settings, and server options. |
| **Configuration Values** | Configuration values are settings that control how an application works without changing its source code. Examples include API keys, database URLs, application environment, server ports, and cache settings. |
| **Environment Variables** | Variables provided outside the source code, commonly used to supply configuration values and sensitive information. |
| **`.env` File** | A file commonly used to store environment variables locally. |

---

## 1. APIRouter — Example

**Project structure:**

```text
fastapi_project/
├── main.py
└── routers/
    └── users.py
```

### Step 1: Create `routers/users.py`

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    return {"message": "List of users"}

@router.post("/users")
def create_user():
    return {"message": "User created"}
```

### Step 2: Connect the router in `main.py`

```python
from fastapi import FastAPI
from routers.users import router as users_router

app = FastAPI()

app.include_router(users_router)
```

### Step 3: Run the application

```bash
uvicorn main:app --reload
```

Open Swagger UI: http://127.0.0.1:8000/docs

### Adding a prefix

```python
app.include_router(users_router, prefix="/api/v1")
```

The endpoints become:

- `GET /api/v1/users`
- `POST /api/v1/users`

A prefix adds a common starting path to routes and can help organize API versions.

---

## 2. Configuration Values

**Definition:** Configuration values are settings that control an application's behavior or operation without requiring changes to its source code.

### Examples

| Configuration value | Purpose |
|---|---|
| `GROQ_API_KEY` | Provides the credential required to access the Groq API. |
| `DATABASE_URL` | Specifies the database connection details. |
| `APP_ENV` | Identifies the environment, such as development or production. |
| `PORT` | Specifies the port on which the server should listen, when the application uses this setting. |
| `LRU_CAPACITY` | Specifies the maximum number of entries allowed in an LRU cache. |
| `LRU_TTL_SEC` | Specifies how long cached entries remain valid, in seconds. |

### Example: `.env` file

```env
GROQ_API_KEY=your-api-key
DATABASE_URL=mysql://user:password@localhost/db
APP_ENV=development
PORT=8000
LRU_CAPACITY=2048
LRU_TTL_SEC=86400
```

**Why use configuration values?**

- **Flexibility:** Change application settings without modifying source code.
- **Environment separation:** Use different settings for development, testing, and production.
- **Security:** Keep sensitive credentials out of source code.
- **Maintainability:** Manage application settings in a consistent way.

**Important:** Environment variables are one way to supply configuration values. A `.env` file is commonly used for local development. Add it to `.gitignore` to avoid committing secrets to GitHub. For production, use the hosting platform's environment-variable or secret-management settings.

<hr>

## Environment Variables
Definition: Environment variables are key-value pairs provided to an application from outside its source code. They are commonly used to supply configuration values, such as API keys, database URLs, and application settings.
1. Why do we use environment variables?
Suppose you are building a FastAPI AI service that uses the Groq API.

You need an API key to access the service.

Without environment variables (hardcoding):

GROQ_API_KEY = "your-secret-api-key"


Here, the secret is written directly in the source code. If you upload this file to GitHub, you could accidentally expose your API key.

With environment variables:


import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


Now, Python reads the API key from the environment instead of storing the actual key in the source code.

<hr>

## 3. How to set environment variables
There are two common approaches.


Method 1: Using a .env file
Create a file named .env in your project directory:
GROQ_API_KEY=your-secret-api-key
APP_ENV=development
PORT=8000


Install python-dotenv:
pip install python-dotenv


Read the values in Python:

```
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
app_env = os.getenv("APP_ENV")

print(app_env)

```

load_dotenv() loads variables from the .env file into the process environment. os.getenv() reads them.


Method 2: Set them directly in the terminal
In Windows PowerShell:
$env:APP_ENV = "development"
$env:PORT = "8000"


Then read them in Python:

import os

print(os.getenv("APP_ENV"))
print(os.getenv("PORT"))