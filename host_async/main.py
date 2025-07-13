import asyncio
import logging
from queries import ORM


async def main():
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("_sqlalchemy.engine").setLevel(logging.INFO)

    orm = await ORM.list_items()
    print("orm:", orm)


if __name__ == "__main__":
    asyncio.run(main())
