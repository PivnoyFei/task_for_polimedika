from asyncio import current_task
from typing import AsyncIterator

import sqlalchemy
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    create_async_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from application.settings import SQLALCHEMY_DATABASE_URI

engine = create_async_engine(SQLALCHEMY_DATABASE_URI)
Base = declarative_base()
metadata = sqlalchemy.MetaData()

async_session = async_scoped_session(
    sessionmaker(engine, expire_on_commit=False, class_=AsyncSession),
    scopefunc=current_task,
)


async def db_session() -> AsyncIterator[AsyncSession]:
    async with async_session() as session:
        yield session
