from sqlalchemy import select
from database import session_factory
from models import Item


class ORM:

    @staticmethod
    def list_items():
        with session_factory() as session:
            query = select(Item.item_id)
            try:
                items = session.execute(query)
                result = items.scalars().all()
            except:
                print("ЕГГОГ")
                result = None
            finally:
                return result
