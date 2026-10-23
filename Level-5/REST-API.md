## 1. What is a REST API?
REST API stands for Representational State Transfer Application Programming Interface.

REST API development means creating APIs that allow different applications to communicate with each other over HTTP.



2. Important REST API concepts
Concept	Meaning	Example
Endpoint	API URL	/articles
HTTP method	Action to perform	GET, POST
Request	Data sent to the backend	Article title
Response	Data returned by backend	Article details
JSON	Common data exchange format	{"title": "AI"}
Status code	Indicates the result	200, 404, 500


## Build your first REST API using FastAPI

*Step 1:* Install FastAPI
Run this in your terminal:
```
pip install fastapi uvicorn
```

*Step 2:* Create main.py

```

from fastapi import FastAPI

app = FastAPI()

articles = [
    {"id": 1, "title": "Introduction to AI"},
    {"id": 2, "title": "Introduction to Python"}
]

@app.get("/")
def home():
    return {"message": "REST API is running"}

@app.get("/articles")
def get_articles():
    return articles

@app.get("/articles/{article_id}")
def get_article(article_id: int):
    for article in articles:
        if article["id"] == article_id:
            return article

    return {"message": "Article not found"}

@app.post("/articles")
def create_article(article: dict):
    articles.append(article)
    return {
        "message": "Article created successfully",
        "article": article
    }
```


*Step 3:* Run the API
```
uvicorn main:app --reload
```

Open these URLs in your browser:
- Home endpoint
- Get all articles
- Interactive API documentation
The /docs page lets you test your API directly using Swagger UI.



## REST API development workflow

1. Define endpoints — decide which operations your application needs.
2. Accept requests — receive parameters and JSON data.
3. Validate input — use Pydantic models in FastAPI.
4. Process business logic — perform calculations, call an AI model, or apply rules.
5. Interact with a database — use MySQL or another database when needed.
6. Return responses — send JSON and suitable HTTP status codes.
7. Test and deploy — use Swagger, Pytest, Docker, and a hosting platform.