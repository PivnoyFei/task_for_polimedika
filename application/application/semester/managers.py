from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.semester.models import Semester
from application.semester.schemas import SemesterCreate


class SemesterManagers:
    @staticmethod
    async def check_name_year(session: AsyncSession, data: SemesterCreate):
        query = await session.execute(
            select(Semester.id).where(
                Semester.curriculum_id == data.curriculum_id,
                Semester.num == data.num,
                Semester.year == data.year,
            )
        )
        return query.scalar()
