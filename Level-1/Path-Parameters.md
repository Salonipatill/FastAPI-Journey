## Path parameters are values included directly in the URL path to identify a specific resource.

GET /users/5

Here:

/users → resource
5 → path parameter (user ID)


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

If you request:

/users/5

FastAPI gives:
user_id = 5