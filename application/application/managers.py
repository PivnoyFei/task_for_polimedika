from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from application.services import limit_offset


class BaseManagers:
    def __init__(self, model: type):
        self.model = model


class Managers(BaseManagers):
    """
    Общий менеджер моделей, позволяет создать любую модель.
    Получить список моделей или одну по id со всеми значениями.
    Получить список с фильтром по имени доступно только для моделей с именем имени (name).
    """

    async def create(self, session: AsyncSession, items: dict):
        query = await session.execute(insert(self.model).values(**items).returning(self.model))
        await session.commit()
        return query.scalar()

    async def get_one(self, session: AsyncSession, pk: int):
        query = await session.execute(select(self.model).where(self.model.id == pk))
        return query.scalar()

    async def get_all(self, session: AsyncSession, page: int, name: str = '') -> tuple[int, list]:
        count, query = await limit_offset(self.model, page)
        if name and hasattr(self.model, 'name'):
            count = count.where(self.model.name.like(f"{name}%"))
            query = query.where(self.model.name.like(f"{name}%"))
        count = await session.execute(count)
        query = await session.execute(query)
        return count.scalar(), list(query.scalars())
