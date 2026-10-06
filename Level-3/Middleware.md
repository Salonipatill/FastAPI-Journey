Middleware is code that runs between the incoming request and the outgoing response.

Client
  ↓
Request
  ↓
Middleware
  ↓
Endpoint
  ↓
Middleware
  ↓
Response
  ↓
Client


Common uses
Logging
Authentication
CORS
Request/response processing
Timing requests
Adding headers

Step 1: Import required classes
from fastapi import FastAPI, Request
FastAPI → creates your application.
Request → gives you access to the incoming HTTP request.
Step 2: Create your FastAPI app
app = FastAPI()
Step 3: Create the middleware

Use:

@app.middleware("http")

Then create an async function:

@app.middleware("http")
async def my_middleware(request: Request, call_next):

At this point:

request → incoming request
call_next → sends the request forward
Step 4: Write what should happen before the endpoint

For example, logging:

print("Request received")

So:

@app.middleware("http")
async def my_middleware(request: Request, call_next):

    print("Request received")
Step 5: Pass the request to the endpoint

This is the most important step:

response = await call_next(request)

It means:

Middleware
    ↓
call_next(request)
    ↓
Endpoint
    ↓
Response
Step 6: Write what should happen after the endpoint

For example:

print("Response generated")

Complete:

@app.middleware("http")
async def my_middleware(request: Request, call_next):

    print("Request received")

    response = await call_next(request)

    print("Response generated")

    return response
Step 7: Return the response

Always return:

return response

Otherwise, your endpoint's response won't be passed back normally.