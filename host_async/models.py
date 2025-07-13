from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True


class Item(Base):
    '''
    Таблица предметов
    '''
    __tablename__ = "items_info"

    item_id: Mapped[int] = mapped_column(primary_key=True)
