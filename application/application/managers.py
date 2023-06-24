from datetime import datetime

from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from application.services import limit_offset
from application.settings import NOT_FOUND


class BaseManagers:
    def __init__(self, model: type):
        self.model = model


class Managers(BaseManagers):
    """Общий менеджер моделей, позволяет создать любую модель.
    Получить список моделей или одну по id со всеми значениями.
    Получить список с фильтром по имени доступно только для моделей с именем имени (name).
    Удалить любую модель и сделать обновление модели
    Пример: variable = Managers(Model), variable.create(session, items)"""

    async def create(self, session: AsyncSession, items: dict) -> type | None:
        query = await session.execute(insert(self.model).values(**items).returning(self.model))
        await session.commit()
        return query.scalar()

    async def get_one(self, session: AsyncSession, pk: int) -> type | None:
        query = await session.execute(select(self.model).where(self.model.id == pk))
        return query.scalar() or NOT_FOUND

    async def get_all(
        self, session: AsyncSession, params: type, attr_name: str
    ) -> tuple[int, list]:
        count, query = await limit_offset(self.model, params)

        if hasattr(params, attr_name) and hasattr(self.model, attr_name):
            if search := getattr(params, attr_name):
                model = getattr(self.model, attr_name)
                count, query = [i.where(model.like(f"{search}%")) for i in (count, query)]
        count, query = await session.execute(count), await session.execute(query)
        return count.scalar(), list(query.scalars())

    async def update(self, session: AsyncSession, items: dict, pk: int) -> type | None:
        try:
            query = await session.execute(
                update(self.model)
                .values(**items, updated_at=datetime.utcnow())
                .where(self.model.id == pk)
                .returning(self.model)
            )
            await session.commit()
            return query.scalar()

        except:
            await session.rollback()
            return None

    async def delete(self, session: AsyncSession, pk: int) -> list:
        query = await session.execute(
            delete(self.model).where(self.model.id == pk).returning(self.model.id)
        )
        await session.commit()
        return query.all()
