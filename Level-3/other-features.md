| Topic                        | Short interview answer                                                                                    |
| ---------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Background Tasks**         | Used to **run tasks after sending the response** without making the client wait.                          |
| **Lifespan Events**          | Used to **run startup and shutdown logic** for the application.                                           |
| **API Versioning**           | Used to **maintain different versions of an API** without breaking existing clients.                      |
| **Logging**                  | Used to **record application events, errors, and useful information** for monitoring and debugging.       |
| **Configuration Management** | Used to **manage application settings** such as database URLs, API keys, and environment-specific values. |


1. Background Tasks

Example:

from fastapi import BackgroundTasks

@app.post("/send")
def send_email(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email_function)
    return {"message": "Email scheduled"}

Remember:

Response first → background task runs.

2. Lifespan Events

Used when something must happen when the application starts or stops.

Application starts
       ↓
Startup logic
       ↓
Application runs
       ↓
Shutdown logic
       ↓
Application stops

Example uses:

Connect to database
Load AI model
Close database connection
Release resources
3. API Versioning

Example:

/api/v1/users
/api/v2/users

It allows you to introduce changes in v2 while keeping v1 working for existing clients.

4. Logging

Example:

import logging

logging.info("User created")
logging.error("Database connection failed")

Used to understand what happened inside the application.

5. Configuration Management

Instead of writing:

DATABASE_URL = "..."

everywhere, keep settings centrally:

.env
   ↓
Configuration
   ↓
FastAPI application

Common settings:

DATABASE_URL
API_KEY
DEBUG
SECRET_KEY