## ASGI=Asynchronous Server Gateway Interface

Web Server

ASGI

Python Web Application



## FastAPI is an ASGI-compatible framework.

## Uvicorn is an ASGI server.

Uvicorn is a web server used to run FastAPI application.

Uvicorn lightweight ASGI server

Used to run Python web applications

Uvicorn is a ASGI sever, and ASGI is interface that Uvicorn uses to communicate with FastAPI.

## Suppose:-

GET/users

Uvicorn receives the HTTP request.
Uvicorn communicates with FastAPI through ASGI.
FastAPI finds the /users route.
Your Python function execute.
FastAPI creates the response.
ASGI provides the communication interface back to Uvicorn.
Uvicorn sends the response to the client.

## Easy memory trick:
Uvicorn = who communicates
ASGI = how they communicate
FastAPI = application being communicated with



## Gateway
Connnection between two sides
Gateway is an architectural concept
gateway can be a separate service/application
a component that manages/controls the path between systems.

## Web server 
A web server is software that receives requests from clients and sends back responses over the web.

## FastAPI → creates the API
FastAPI is a Python web framework used to create APIs.

FastAPI provides functionality such as:
Creating API routes
Handling HTTP methods(GET, POST, PUT, DELETE)
Request validation
Response handling
Python type-hint based validation
Automatic Swagger/OpenAPI documentation
Dependency injection
Websocket support


## Uvicorn → runs/serves the API
Uvicorn runs the API and communicates with the network.

Starts a server.
Listens for incoming connections.
Receives HTTP/WebSocket requests.
Communicates with your FastAPI application through ASGI.
Sends the response back to the client.

## Compatible means able to work together properly without causing problems.
FastAPI ↔ Uvicorn
FastAPI is designed to work with ASGI servers such as Uvicorn.
astAPI and Uvicorn are compatible.
Uvicorn can run a FastAPI application because they follow the same ASGI interface.

## A message is the actual piece of information being sent.
## An event means something happened, and the message describes what happened.

ASGI events are Python dictionaries containing information about what is happening in the connection.