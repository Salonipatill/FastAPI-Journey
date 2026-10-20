| Topic                     | Interview answer                                                                                         |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| **APIRouter**             | `APIRouter` is used to **group related API routes**. 

APIRouter is a FastAPI class used to organize API endpoints into separate, reusable groups instead of writing all routes in one file.  

fastapi_project/

main.py — Main application

routers/

users.py — User endpoints

summarize.py — Summarization endpoints 


## Step 1: Create routers/users.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    return {"message": "List of users"}

@router.post("/users")
def create_user():
    return {"message": "User created"}    
    
    
    
## Step 2: Connect the router in main.py   

```
from fastapi import FastAPI
from routers.users import router as users_router

app = FastAPI()

app.include_router(users_router)  

```

```
uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs to test the endpoints.


## 3. How to add a prefix

```
app.include_router(
    users_router,
    prefix="/api/v1"
)
```


Now the endpoints become:
- GET /api/v1/users
- POST /api/v1/users


The prefix helps you organize API versions and endpoint paths.
                                  |
| **Routers**               | Routers contain **endpoint definitions** and handle HTTP requests.                                       |

| **Modular Architecture**  | It means **dividing a large application into separate modules** for better organization and maintenance. [Done]|

| **Services**              | Services contain the **business logic** of the application.                                          [Done]|

| **Schemas**               | Schemas define and **validate the data** received from or returned by the API. [Done] |   
                      |

| **Models**                | Models represent **database tables and their data**.                                                     |

| **Configuration**         | Configuration manages **application settings** such as database URLs and API settings.    


**Configuration values** are settings that control how an application works without changing its source code.

For example, in your FastAPI AI service, you might want to change the API key, database URL, or server port. These are configuration values.

**Example:-**

GROQ_API_KEY=abc123
APP_ENV=development
PORT=8000  
          |
| **Environment Variables** | Variables provided outside the code, commonly used for **configuration and sensitive values**.           |


| **`.env`**                | A file commonly used to **store environment variables locally**.   [Done]                                      |
