Interview Question: What is a Response in FastAPI?
A response is the server's reply sent back to the client after receiving and processing a request. It contains a status code, headers, and a body that may carry data or a message.

Example: When a client requests student details, FastAPI returns the student's data along with a status code such as 200 OK.
Related interview questions
1. What are the main components of an HTTP response?

An HTTP response has three main components:
- Status code: Indicates the result of the request.
- Headers: Provide metadata about the response.
- Body: Contains the response data, such as JSON.
2. What is a response status code?

A status code is a three-digit number that indicates the outcome of an HTTP request, such as 200 for success or 404 when a resource is not found.

3. What is the difference between a request and a response?

A request is sent by the client to ask the server for a resource or action. A response is sent by the server back to the client with the result.

4. How does FastAPI send a response?

FastAPI can return Python data, such as dictionaries, which it typically serializes into JSON responses automatically.
from fastapi import FastAPIapp = FastAPI()@app.get("/student")def get_student():    return {"name": "Saloni", "course": "B.Tech"}



Here, the server returns student details as a JSON response.

5. What is the difference between response headers and response body?

Response headers contain metadata, such as the content type. The response body contains the actual data returned by the server.

Remember for interviews: Request = client sends data or asks for an action. Response = server returns the result.