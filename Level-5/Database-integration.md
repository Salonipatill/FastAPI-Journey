## Database integration means connecting your Python backend to a database so that your API can store, retrieve, update, and delete data permanently.

For your Python Developer and AI Engineer path, we'll use FastAPI + MySQL + SQLAlchemy.


## Understand the three important terms
- MySQL: The database that stores your data.
- SQLAlchemy: A Python library that helps your code interact with a database using Python objects and SQL.
- ORM: Object-Relational Mapping. It lets you work with database tables using Python classes instead of writing every SQL query manually.
For example, a Python class called Article can represent an articles table in MySQL.


## 3. Create a MySQL database
Open MySQL Workbench or your MySQL terminal and run:

```
CREATE DATABASE news_db;
```

This creates an empty database named news_db.


## 4. Install the required Python libraries

Run:

```
pip install fastapi uvicorn sqlalchemy pymysql
```


PyMySQL is the driver SQLAlchemy uses to communicate with MySQL.


## 5. Connect FastAPI to MySQL

Create a file named database.py.

```

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = (
    "mysql+pymysql://root:YOUR_PASSWORD@localhost/news_db"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

Replace YOUR_PASSWORD with your MySQL password. In real projects, keep credentials in environment variables rather than committing them to GitHub.


Understand the code
Code	Purpose
create_engine()	Configures database connectivity
sessionmaker()	Creates database sessions
SessionLocal()	Opens a session for database operations
Base	Parent class for database models
get_db()	Provides a session and closes it afterward


A database session is the unit of work your code uses to perform database operations. FastAPI's dependency injection can provide a session to each request handler and ensure it gets closed.




### 6. Create a database table using Python
Create main.py in the same folder.

```

from fastapi import FastAPI, Depends
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from database import Base, engine, get_db

app = FastAPI()

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(String(2000), nullable=False)


Base.metadata.create_all(bind=engine)


@app.post("/articles")
def create_article(
    title: str,
    content: str,
    db: Session = Depends(get_db)
):
    article = Article(title=title, content=content)

    db.add(article)
    db.commit()
    db.refresh(article)

    return {
        "id": article.id,
        "title": article.title,
        "content": article.content
    }
```


Here's what happens:
1. Article defines the database table structure.
2. create_all() creates the table if it doesn't exist.
3. Depends(get_db) gives the endpoint a database session.
4. db.add(article) stages the new article for insertion.
5. db.commit() saves the change to MySQL.
6. db.refresh(article) retrieves database-generated values, such as the new ID.


## 7. Test your API

Run the application:
```
uvicorn main:app --reload
```

Open FastAPI Swagger documentation.


## You can then check MySQL:
```
USE news_db;

SELECT * FROM articles;
```

Your saved article should appear in the results.