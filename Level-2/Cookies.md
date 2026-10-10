A cookie is a small piece of data that a website/server asks the browser to store and send back with future requests.

In FastAPI, cookies are used to store small pieces of data in the user's browser and send them automatically with subsequent HTTP requests to the same website.

| Cookie                              | Request Body                        |
| ----------------------------------- | ----------------------------------- |
| Small data sent with requests       | Main data being submitted           |
| Stored by browser                   | Usually sent as part of the request |
| Often used for sessions/preferences | Used for creating/updating data     |
| Example: `session_id=abc123`        | Example: `{"name":"Saloni"}`        |


1. What is the role of cookies in FastAPI?
Cookies are mainly used for:
1. Authentication — to maintain a user's login session.
2. Session management — to remember that a user is logged in.
3. Personalization — to remember user preferences, such as language or theme.
4. Tracking preferences — to remember settings between requests.


````
from fastapi import FastAPI, Response, Cookie

app = FastAPI()

# Set a cookie
@app.get("/login")
def login(response: Response):
    response.set_cookie(
        key="username",
        value="Saloni",
        httponly=True
    )
    return {"message": "Login successful"}


# Read a cookie
@app.get("/profile")
def profile(username: str | None = Cookie(default=None)):
    return {"username": username}
```   


4. Important cookie settings
Setting	Role
key	Cookie name
value	Data stored in the cookie
httponly=True	Prevents JavaScript from reading the cookie
secure=True	Sends the cookie only over HTTPS
samesite	Controls cross-site cookie sending
max_age	Sets how long the cookie lasts, in seconds


Remember the difference:
- Response.set_cookie() → sets a cookie.
- Cookie() → reads a cookie from the request.



```
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/logout")
def logout(response: Response):
    response.delete_cookie(key="username")
    return {"message": "Cookie deleted"}
```


4. Cookies with a frontend and FastAPI backend
Suppose your frontend runs on localhost:3000 and FastAPI runs on localhost:8000.
To allow the frontend to make credentialed requests:
from fastapi.middleware.cors import CORSMiddlewareapp.add_middleware(    CORSMiddleware,    allow_origins=["http://localhost:3000"],    allow_credentials=True,    allow_methods=["*"],    allow_headers=["*"],)



The frontend must also send credentials, for example:
fetch("http://localhost:8000/profile", {
    credentials: "include"
});


Important details:
- The backend must set appropriate cookie attributes.
- Credentialed CORS requests require a specific allowed origin, not "*".
- localhost and 127.0.0.1 are different hosts.
- SameSite, Secure, browser privacy rules, and the request context can affect whether the cookie is sent.


### CSRF (Cross-Site Request Forgery) is a security attack in which an attacker tricks a logged-in user’s browser into sending an unwanted request to a website where the user is already authenticated.


3. Easy example
Imagine your FastAPI website is mybank.com.
- samesite="strict" — restricts the bank's cookie from being sent in cross-site contexts.
- samesite="lax" — allows the cookie in certain situations, such as following a normal link to the bank.
- samesite="none" — permits cross-site cookie sending when other requirements are met.


Q1. What are cookies?
Answer: Cookies are small pieces of data stored in the user's browser. They help websites remember information such as login sessions and user preferences.

Q2. Why do we use cookies in FastAPI?
Answer: We use cookies for session management, authentication, and storing user preferences. FastAPI allows us to set, read, and delete cookies.



Quick revision: Important syntax
Task	FastAPI syntax
Set a cookie	response.set_cookie()
Read a cookie	Cookie()
Delete a cookie	response.delete_cookie()
Restrict JavaScript access	httponly=True
Require HTTPS	secure=True
Control cross-site sending	samesite="lax"
Set lifetime	max_age=3600