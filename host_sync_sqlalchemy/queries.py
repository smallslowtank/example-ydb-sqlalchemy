from sqlalchemy import select
from database import session_factory
from models import User


class ORM:

    @staticmethod
    def list_users():
        with session_factory() as session:
            stmt = select(User.user_id)
            try:
                list_users = session.execute(stmt)
                result = list_users.scalars().all()
            except Exception as e:
                print(e)
                result = None
            return result
