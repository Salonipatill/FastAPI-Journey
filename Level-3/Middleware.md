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