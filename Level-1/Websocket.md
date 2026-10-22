## How to create a WebSocket in FastAPI

*Step 1: Install the required packages*

```
pip install fastapi uvicorn
```

*Step 2: Create main.py*

Write the following code:
```
from fastapi import FastAPI, WebSocket, WebSocketDisconnectapp = FastAPI()
@app.websocket("/chat")
async def chat(websocket: WebSocket):   
 await websocket.accept() 

    try:        while True:            message = await websocket.receive_text()        
        await websocket.send_text(f"Received: {message}")  
          except WebSocketDisconnect:        print("Client disconnected")

```

*Step 3: Understand each line*

Code	Meaning
from fastapi import FastAPI, WebSocket	Imports the required classes
app = FastAPI()	Creates the FastAPI application
@app.websocket("/chat")	Registers the WebSocket endpoint at /chat
async def chat(websocket: WebSocket):	Defines the asynchronous handler
await websocket.accept()	Accepts the incoming connection
await websocket.receive_text()	Waits for a text message
await websocket.send_text(...)	Sends a text message back
while True:	Repeats the receive-and-send process
except WebSocketDisconnect:	Handles a disconnected client

Step 4: Run the application
uvicorn main:app --reload


The server runs at http://127.0.0.1:8000, and the WebSocket endpoint is ws://127.0.0.1:8000/chat.

To test it, open the browser's Developer Tools → Console and run:
const ws = new WebSocket("ws://127.0.0.1:8000/chat");

ws.onopen = () => ws.send("Hello!");
ws.onmessage = (event) => console.log(event.data);


Expected output:
Received: Hello!



How do you create a WebSocket in FastAPI?

"First, I import FastAPI and WebSocket. Then, I register an endpoint using @app.websocket(). Inside the asynchronous function, I accept the connection using await websocket.accept(). I use receive_text() to receive messages and send_text() to send responses. Finally, I handle client disconnections using WebSocketDisconnect."