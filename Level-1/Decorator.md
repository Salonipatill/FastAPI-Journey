## Decorator (@)  in Python
A decorator adds extra behavior to a function without changing its main code.
In FastAPI: Decorators register **a function** as an *API endpoint* and define its HTTP method and URL path.
Example:

```
@app.get("/")def home():  
        return {"message": "Hello World"}
```

@app.get("/") — A route decorator that registers a function to handle HTTP GET requests at the root path (/) 
- home() — Executes when a matching request is received.










Convert to PDF