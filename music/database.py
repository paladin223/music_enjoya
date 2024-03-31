import asyncio

from config import settings
from sqlalchemy import create_engine
from sqlalchemy import text
# from sqlalchemy import URL
# from sqlalchemy.ext.asyncio import async_sessionmaker
# from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

# from sqlalchemy.orm import Session
# from sqlalchemy.orm import sessionmaker

sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    # echo=True,
    # pool_size=5,
    # max_overflow=10,
)


async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    # echo=True,
    # pool_size=5,
    # max_overflow=10,
)

# with sync_engine.connect() as conn:
#     res = conn.execute(text("SELECT VERSION();"))
#     print(f"{res.first()=}")


async def get_123():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT 1, 2, 3 union select 4, 5, 6"))
        print(f"{res.first()=}")


asyncio.run(get_123())
