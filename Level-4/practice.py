#Task 1-Fetch Product
import asyncio

async def get_product():
    print("Fetching product.....")
    await asyncio.sleep(2)
    return  "Laptop"


async def main():
     result= await get_product()

     print(result)


asyncio.run(main())

     
