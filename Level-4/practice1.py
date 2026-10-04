import asyncio
async def user():
    print("user details")
    await asyncio.sleep(3)
    return "User"



async def product():
        print("product details")
        await asyncio.sleep(3)
        return "product"


async def order():
      print("order details")
      await asyncio.sleep(3)
      return "order"


async def main():
      result= await asyncio.gather(
            product(),
            user(),
            order()
      )

      return result


asyncio.run(main())