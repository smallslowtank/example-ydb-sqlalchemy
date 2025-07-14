from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True


class User(Base):
    '''
    Таблица пользователей
    '''
    __tablename__ = "Users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
