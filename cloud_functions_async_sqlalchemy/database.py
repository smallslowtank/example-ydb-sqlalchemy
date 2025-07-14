from sqlalchemy import AsyncAdaptedQueuePool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import settings

engine = create_async_engine(url=settings.url, poolclass=AsyncAdaptedQueuePool, **settings.args)
session_factory = async_sessionmaker(bind=engine)
