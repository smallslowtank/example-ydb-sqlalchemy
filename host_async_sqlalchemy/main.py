import asyncio
from queries import ORM


async def main():
    query = await ORM.list_users()
    print("Users:", query)


if __name__ == "__main__":
    asyncio.run(main())
