Synchronous = wait for one task to finish
Asynchronous = don't waste time waiting; work on another task

asyncio is a Python library/module used to run asynchronous code.


async programming is designed specifically to avoid unnecessary waiting.

await gets the result from that asynchronous operation.

await waits for an asynchronous operation to produce its result, while allowing other async work to proceed.

await is used inside an async def function.

asyncio.run() starts and runs an asynchronous function and manages the event loop for it.


| Keyword / Function | Specific use                           | Simple meaning                           |
| ------------------ | -------------------------------------- | ---------------------------------------- |
| `async`            | Creates an asynchronous function       | "This function can work asynchronously." |
| `await`            | Waits for an async operation to finish | "Give me its result."                    |
| `asyncio`          | Python module for managing async tasks | "Tools for async programming."           |
| `asyncio.sleep()`  | Creates an asynchronous wait           | "Wait without blocking other tasks."     |
| `asyncio.run()`    | Starts an async program                | "Run my async function."                 |
| `asyncio.gather()` | Runs multiple async tasks concurrently | "Run these tasks together."              |




Let's learn asyncio.gather() from zero, using the same style as your previous async/await practice.

1. First understand the problem

Suppose we have two functions:

async def get_user():
    await asyncio.sleep(2)
    return "User received"

async def get_product():
    await asyncio.sleep(3)
    return "Product received"

If we do this:

async def main():
    user = await get_user()
    product = await get_product()

The execution is:

get_user
   ↓
wait 2 seconds
   ↓
get_product
   ↓
wait 3 seconds
   ↓
Total ≈ 5 seconds

Why?

Because the second function starts only after the first one finishes.

2. What does gather() do?

asyncio.gather() allows us to start multiple async functions together.

await asyncio.gather(
    get_user(),
    get_product()
)

Now:

get_user     ──────────→ 2 sec ✓
get_product  ───────────────→ 3 sec ✓
               START TOGETHER

Total time ≈ 3 seconds, because we wait for the slowest task.