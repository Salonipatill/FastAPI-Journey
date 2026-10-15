Redis is a very fast in-memory data store. It is commonly used as a cache, but it can also be used for sessions, queues, rate limiting, and other temporary/fast-access data.

Think of Redis as a **very fast temporary storage area** for your application.

### Redis stands for Remote Dictionary Server.


### Simple example
Imagine you are using a website that shows AI-generated summaries.
- The first time you request a summary, the AI model generates it.
- FastAPI saves the summary in Redis.
- The next time you request the same summary, FastAPI retrieves it from Redis instead of calling the AI model again.
This makes your application faster and can reduce AI API costs.

disk primarily keeps frequently accessed data in RAM (memory).

RAM is much faster to access than traditional disk-based storage.


| Redis                               | MySQL                                                   |
| ----------------------------------- | ------------------------------------------------------- |
| Primarily in-memory                 | Primarily disk-backed persistent database               |
| Extremely fast                      | Generally slower than Redis for simple key-value access |
| Often used for cache                | Used for permanent application data                     |
| Key-value and other data structures | Relational database                                     |
| Temporary/frequently accessed data  | Users, orders, articles, etc.                           |



Redis – Interview Preparation
## 1. What is Redis?
answer:
Redis is an open-source, in-memory data store used for caching and fast data access. It stores data in memory, so retrieving data is generally faster than retrieving it from a disk-based database.


## 2. Why do we use Redis?
Redis is used to:
1. Caching: Store frequently accessed data to improve performance.
2. Rate limiting: Restrict the number of API requests a user can make.
3. Session management: Store temporary session information.
4. Temporary storage: Store data such as OTPs with an expiration time.


## 4. What is caching?
answer: Caching is the process of storing frequently used data temporarily so that it can be accessed quickly when needed again.
Example: If a user requests the same AI summary twice, Redis can return the saved summary instead of generating it again.



### 5. Redis vs MySQL
Redis	MySQL
Primarily an in-memory data store	Relational database
Optimized for fast data access	Designed for structured relational data
Commonly used for caching	Commonly used for permanent records
Supports expiration of keys	Supports persistent database records
Redis can also persist data when configured, so it is not exclusively a temporary store.


## 6. Is Redis mandatory in FastAPI?
No. FastAPI works without Redis. Redis is an additional service that you use when your application needs caching, shared session data, rate limiting, or other supported capabilities.



## Is Redis mandatory in FastAPI? Why or why not?
No, Redis is not mandatory in FastAPI. It is an optional service used for caching, rate limiting, and session management. We use Redis when our application needs fast, shared data storage, but we can also build FastAPI applications without it.

Redis is not mandatory even when you need caching. You can also use an in-memory Python dictionary or another caching solution, depending on your requirements.


### Evaluation: Cache Hit vs Cache Miss
A cache hit occurs when the requested data is already available in the cache, so we can return it directly.

A cache miss occurs when the requested data is not available in the cache, so we need to fetch or generate the data and may store it in the cache for future use.


## working example.

## 1. Install Redis package

pip install fastapi uvicorn redis


##  2. Write the FastAPI code

````

from fastapi import FastAPI
import redis.asyncio as redis
import json

app = FastAPI()

# Connect to Redis
r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

@app.get("/summary")
async def get_summary(text: str):

    # Create a unique cache key for this text
    cache_key = f"summary:{text}"

    # Step 1: Check Redis
    cached_summary = await r.get(cache_key)

    # Step 2: If cache hit
    if cached_summary:
        return {
            "source": "Redis Cache",
            "summary": json.loads(cached_summary)
        }

    # Step 3: If cache miss, generate a result
    # Demo result; replace with your AI model call
    summary = f"Summary of: {text}"

    # Step 4: Save result in Redis for 1 hour
    await r.set(
        cache_key,
        json.dumps(summary),
        ex=3600
    )

    # Step 5: Return result
    return {
        "source": "AI Model",
        "summary": summary
    }
```
###  3. How to test it
Run your application:
uvicorn main:app --reload


In a typical FastAPI application, FastAPI and Redis use different ports.
Service	Default port	Purpose
FastAPI (Uvicorn)	8000	Receives HTTP requests
Redis	6379	Stores and retrieves data


Remember:
- Function call: parameter=value
- Dictionary: key: value


4. Why write each argument on a separate line?
Python allows both formats:
r = redis.Redis(host="localhost", port=6379)



Or:
r = redis.Redis(    host="localhost",    port=6379,    decode_responses=True)



