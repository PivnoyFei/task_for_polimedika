from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from application.student.models import Student
from application.student.schemas import StudentCreate


async def get_student(session: AsyncSession, pk: int | None = None, name: str = "") -> Student:
    query = select(Student.id)
    query = await session.execute(query)
    return query.all()


async def create(student: StudentCreate, session: AsyncSession) -> Student:
    query = await session.execute(
        insert(Student)
        .values(
            first_name=student.first_name,
            last_name=student.last_name,
            description=student.description,
            is_learn=student.is_learn,
            group_id=None,
        )
        .returning(Student)
    )
    await session.commit()
    return query.one()
