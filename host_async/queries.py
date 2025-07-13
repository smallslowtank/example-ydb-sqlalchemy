from sqlalchemy import select
from database import session_factory
from models import Item


class ORM:

    @staticmethod
    async def list_items():
        async with session_factory() as session:
            query = select(Item.item_id)
            try:
                items = await session.execute(query)
                result = items.scalars().all()
            except Exception as e:
                print(f"ЕГГОГ!!!\n{e}")
                result = None
            finally:
                return result
