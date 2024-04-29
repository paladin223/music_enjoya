from typing import Annotated

from sqlalchemy import create_engine
from sqlalchemy import Integer
from sqlalchemy import String
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import URL
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
# from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import sessionmaker

from config import settings

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

session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)


str256 = Annotated[str, 256]
intpk = Annotated[int, mapped_column(primary_key=True)]


class Base(DeclarativeBase):
    type_annotation_map = {str256: String(256), intpk: Integer}
