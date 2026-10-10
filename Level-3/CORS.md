# CORS stands for Cross-Origin Resource Sharing. It’s a browser security mechanism that controls whether a web page from one origin can make requests to another origin.


origin consists of three parts:Protocol + Domain + Port
```
http://localhost:3000
- http → Protocol
- localhost → Domain/host
- 3000 → Port
```


## If interviewer asks: "How do you connect frontend with FastAPI backend?"
You can answer:
```
"First, I run my frontend and FastAPI backend. If they are running on different origins, I configure CORS in FastAPI using CORSMiddleware. I add the frontend URL in allow_origins. Then the frontend can make API requests to the FastAPI backend."
```


```
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```


## 1. How to use allow_methods
```
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(    
    CORSMiddleware,  
  allow_origins=["http://localhost:3000"], 
   allow_methods=["GET", "POST", "DELETE"],   
    allow_headers=["*"],
    )
```


This means the frontend at localhost:3000 can make:

```
GET     → allowed
POST    → allowed
DELETE  → allowed
PUT     → NOT allowed
PATCH   → NOT allowed
```

### 2. How to add data from the frontend
Suppose your backend has:

```
from fastapi import FastAPI

app = FastAPI()

@app.post("/users")
def add_user(name: str):  

  return {"message": f"{name} added"}
```

The frontend can send a POST request:
```
fetch("http://localhost:8000/users?name=Saloni", {
    method: "POST"
})
```

Flow:

```
Frontend
   │
   │ POST
   │ name = Saloni
   ▼
FastAPI
   │
   ▼
add_user()
   │
   ▼
{"message": "Saloni added"}
```

So:
POST is generally used to send/create data.

### 3. How to delete data from the backend

## Create a DELETE endpoint:

@app.delete("/users/{user_id}")
def delete_user(user_id: int):   
 return {"message": f"User {user_id} deleted"}


## Frontend:
fetch("http://localhost:8000/users/10", {
    method: "DELETE"
})

## The backend receives:
DELETE /users/10

and runs:
delete_user(10)


So:
DELETE is generally used to remove data


## 6. What does "*" mean?

```
allow_methods=["*"]
```


means:
Allow all HTTP methods for CORS.



## Interview-ready answer
If the interviewer asks:
"How do you allow or restrict HTTP methods using CORS in FastAPI?"
Say:
"allow_methods in CORSMiddleware specifies which HTTP methods are permitted for cross-origin browser requests. For example, allow_methods=['GET', 'POST'] allows the frontend to read and create data but doesn't grant CORS permission for PUT or DELETE. If I use ['*'], all methods are allowed by CORS."


## Part 1 — Basic CORS
## 1. What is CORS?
Interviewer: What is CORS?
You:
“CORS stands for Cross-Origin Resource Sharing. It is a browser security mechanism that allows or restricts requests from one origin to another origin. In FastAPI, we configure CORS using CORSMiddleware.”

Example:
Frontend → http://localhost:3000
Backend  → http://localhost:8000

These are different origins, so CORS may be involved.

## Same-Origin Policy

Same-Origin Policy is a browser security mechanism that restricts JavaScript from freely accessing resources from a different origin. CORS provides a controlled way for a server to allow specific cross-origin access."

Easy memory trick:
SOP = default restriction
CORS = controlled permission


## 2. Why do we need CORS?
Interviewer: Why do we need CORS?
You:
“Browsers follow the same-origin policy. By default, JavaScript from one origin cannot freely access resources from another origin. CORS allows the backend to explicitly tell the browser which origins are permitted.”

Simple idea:
Frontend
localhost:3000
       ↓
    Browser
       ↓
FastAPI
localhost:8000

Because the origins are different, CORS rules apply.


## 3. What is an origin?
Interviewer: What is an origin?
You:
“An origin is made up of the protocol, host, and port.”

For example:
http://localhost:3000

contains:
http       → protocol
localhost  → host
3000       → port

If any of these changes, the origin can become different.



### 4. Are these two URLs the same origin?
http://localhost:3000
http://localhost:8000

You:
“No. They have the same protocol and host, but different ports, so they are different origins.”


## 5. What about these?
http://example.com
https://example.com

You:
“They are different origins because the protocols are different: HTTP versus HTTPS.”


### 6. What is Same-Origin Policy?
Interviewer: What is the same-origin policy?
You:
“Same-origin policy is a browser security rule that restricts a webpage's JavaScript from accessing resources from a different origin unless the server permits it through mechanisms such as CORS.”

Don't say that it means different websites cannot communicate at all. That's too broad.


## 7. Who actually enforces CORS?
Interviewer: Does FastAPI enforce CORS?
Better answer:
“The browser enforces CORS. The backend, such as FastAPI, sends the CORS response headers that tell the browser which cross-origin requests are allowed.”

This is an important interview point.
FastAPI
  │
  │ sends CORS headers
  ▼
Browser
  │
  │ checks the headers
  ▼
Allows / blocks frontend access


## Part 2 — FastAPI CORS

## 8. How do you configure CORS in FastAPI?
You:
“I use FastAPI's CORSMiddleware and configure the allowed origins, methods, headers, and credentials.”

```
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

## 9. How do you add a frontend URL to FastAPI?
Interviewer: My React application is running on localhost:3000. How do you allow it?


## You:
allow_origins=["http://localhost:3000"]


## Complete:

app.add_middleware(  
      CORSMiddleware,   
      allow_origins=["http://localhost:3000"], 
      allow_methods=["*"],   
     allow_headers=["*"],
     )


## Then say:
“This tells the browser that requests coming from that frontend origin can be permitted by the backend's CORS policy.”


## 10. What is CORSMiddleware?
You:
“CORSMiddleware is FastAPI middleware that handles CORS-related request and response processing and adds the appropriate CORS headers.”


## 11. What is allow_origins?
You:
“allow_origins specifies which origins are allowed to make cross-origin browser requests to my backend.”

Example:
allow_origins=[    "http://localhost:3000",    "http://localhost:5173"]


Means those frontend origins are allowed.


## 12. What is allow_methods?
You:
“allow_methods specifies which HTTP methods are allowed for cross-origin requests.”

Example:
allow_methods=["GET", "POST"]


## 13. What is allow_headers?
You:
“allow_headers specifies which request headers the browser is allowed to use for cross-origin requests.”

For example:
allow_headers=[    "Content-Type",    "Authorization"]


This is particularly relevant when your frontend sends an authentication token.



14. What is allow_credentials?
You:
“allow_credentials allows cross-origin requests to include credentials such as cookies or certain authentication credentials.”

Example:
allow_credentials=True


And when credentials are involved, don't blindly use:
allow_origins=["*"]


Use the specific trusted frontend origin.
Part 3 — Connecting Frontend and Backend
15. How do you connect a React frontend to FastAPI?
Interviewer: Explain the complete process.
You:
“First I run my FastAPI backend on a URL such as http://localhost:8000. Then I run my React frontend, for example on http://localhost:3000. If they have different origins, I configure CORS in FastAPI using CORSMiddleware and add the frontend origin to allow_origins. Then the frontend can make API requests to the FastAPI endpoints.”

Example:
allow_origins=["http://localhost:3000"]


Frontend:
fetch("http://localhost:8000/users")

Backend:
@app.get("/users")def get_users():    return {"users": ["Saloni", "Rahul"]}


Part 4 — HTTP Methods
16. How do you add data from frontend to backend?
Use POST.
Backend:
@app.post("/users")def create_user():    return {"message": "User created"}


Frontend:
fetch("http://localhost:8000/users", {
    method: "POST"
})

Interview answer:
“I generally use a POST request to send or create data on the backend.”

17. How do you delete data?
Backend:
@app.delete("/users/{user_id}")def delete_user(user_id: int):    return {"message": f"User {user_id} deleted"}


Frontend:
fetch("http://localhost:8000/users/10", {
    method: "DELETE"
})

Interview answer:
“I create a DELETE endpoint in FastAPI and call that endpoint from the frontend using the DELETE HTTP method.”

18. How do you allow only GET and POST?
allow_methods=["GET", "POST"]


Interview answer:
“I explicitly specify the methods I want to allow in allow_methods. Methods not included in the CORS policy aren't allowed for cross-origin browser requests.”

19. How do you allow everything?
allow_methods=["*"]


Interview answer:
“The wildcard allows all HTTP methods under the CORS policy.”

Part 5 — CORS Scenario Questions
20. The frontend shows a CORS error. What do you check?
This is a very good interview question.
Answer:
“First I check the frontend origin. Then I check whether that origin is included in allow_origins. I check whether the HTTP method is allowed, whether required headers are allowed, and whether the backend is correctly returning the required CORS headers. I also check whether a preflight OPTIONS request is failing.”

Think:
1. Origin?
2. Method?
3. Headers?
4. Credentials?
5. OPTIONS/preflight?
6. Backend CORS configuration?

21. What is a preflight request?
You:
“A preflight request is an OPTIONS request that the browser sends before certain cross-origin requests to check whether the server allows the requested origin, method, and headers.”

Example:
OPTIONS /users
Origin: http://localhost:3000
Access-Control-Request-Method: DELETE

The backend responds with appropriate CORS headers.
22. Why does the browser send OPTIONS?
You:
“The browser uses the preflight OPTIONS request to ask the server for permission before sending certain cross-origin requests.”

Think of it like:
Browser:
"Can I send DELETE from localhost:3000?"

        ↓

Backend:
"Yes, DELETE is allowed."

        ↓

Browser:
"Okay, I'll send the actual request."

23. What is Access-Control-Allow-Origin?
You:
“It is a response header that tells the browser which origin is permitted to access the response.”

Example:
Access-Control-Allow-Origin: http://localhost:3000

24. What is Access-Control-Allow-Methods?
You:
“It is a response header that tells the browser which HTTP methods are permitted for cross-origin requests.”

Example:
Access-Control-Allow-Methods: GET, POST, DELETE

25. What is Access-Control-Allow-Headers?
You:
“It tells the browser which request headers are permitted for the cross-origin request.”

Example:
Access-Control-Allow-Headers: Authorization, Content-Type

Part 6 — Very Important Advanced Questions
26. Does CORS protect my API from Postman?
Interviewer: If I don't allow an origin, can someone still call my API using Postman?
You:
“Yes. CORS is enforced by browsers. Postman, curl, or another backend service isn't subject to browser CORS enforcement. So CORS should not be treated as API authentication or authorization.”

⭐ Remember this one.
27. Is CORS authentication?
You:
“No. CORS and authentication solve different problems. CORS controls whether browser-based cross-origin requests can be accessed. Authentication verifies who the user or client is.”

28. Is CORS authorization?
You:
“No. Authorization determines what an authenticated user is allowed to do. CORS is about browser cross-origin access.”

For example:
Authentication → Who are you?
Authorization  → What are you allowed to do?
CORS           → Can this browser origin access the response?

29. Can CORS stop someone from deleting data?
This is a tricky question.
Don't say simply "yes."
Say:
“CORS can restrict a browser frontend from making a cross-origin DELETE request according to the CORS policy, but it should not be used as the security mechanism for protecting deletion. The backend should use authentication and authorization to decide whether the user is actually allowed to delete the data.”

That's a much stronger answer.
