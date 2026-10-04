## Need to learn from youtube

Dependency Injection means giving a function the thing it needs from outside instead of making the function create it itself.

In FastAPI, we use Depends() to declare these dependencies, and FastAPI automatically executes them and injects their results into the endpoint.


Dependency Injection is a mechanism where the dependencies required by an endpoint are provided from outside instead of being created inside the endpoint. In FastAPI, we use Depends() to declare these dependencies, and FastAPI automatically executes them and injects their results into the endpoint.


def get_db():
    return "Database"


@app.get("/users")
def get_users(db = Depends(get_db)):
    return {"database": db}





Common reusable dependencies

In real FastAPI projects, you commonly create dependencies for:

Database sessions
Current user
Authentication
Authorization
Admin checking
Request validation
Configuration/settings
Services
