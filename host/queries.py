import sqlalchemy as sa
from sqlalchemy import select
from database import session_factory
from models import Users


class ORM:

    @staticmethod
    def list_users():
        with session_factory() as session:
            # SELECT user_id FROM Users
            query = select(Users.user_id)
            users = session.execute(query)
            result = users.scalars().all()
            return result


def run_example_core(engine):
    with engine.connect() as conn:
        # raw sql
        rs = conn.execute(
            sa.text(
                """
                SELECT user_id
                FROM Users
                """
            )
        )
        return rs.scalars().all()
