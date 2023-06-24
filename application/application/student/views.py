from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from application.database import db_session
from application.student.managers import create, get_student
from application.student.schemas import StudentCreate

router = APIRouter()
SESSION = Depends(db_session)


@router.get("/")
async def students(session: AsyncSession = SESSION):
    return await get_student(session)


@router.post("/")
async def create_students(student: StudentCreate, session: AsyncSession = SESSION):
    print("===", student)
    return await create(student, session)
