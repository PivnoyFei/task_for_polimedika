from typing import Any

from fastapi import APIRouter, Depends, Query, Request
from fastapi import status as S
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from application.course.managers import FacultyManagers
from application.course.models import Curriculum, Faculty, Semester
from application.course.schemas import (
    CurriculumCreate,
    CurriculumOut,
    FacultyCreate,
    FacultyOut,
    SemesterCreate,
    SemesterOut,
)
from application.database import db_session
from application.managers import Managers
from application.schemas import Result
from application.services import get_result

router = APIRouter()
SESSION: AsyncSession = Depends(db_session)
faculty = Managers(Faculty)
curriculum = Managers(Curriculum)
semester = Managers(Semester)


@router.post("/faculty/", response_model=FacultyOut, status_code=S.HTTP_201_CREATED)
async def create_faculty(data: FacultyCreate, session: AsyncSession = SESSION) -> JSONResponse:
    """Создать факультет."""
    return await faculty.create(session, data.dict())


@router.get("/faculty/", response_model=Result[FacultyOut], status_code=S.HTTP_200_OK)
async def get_faculties(
    request: Request,
    page: int = Query(1, ge=1, description="Page offset"),
    name: str = Query(None),
    session: AsyncSession = SESSION,
) -> JSONResponse:
    """Получить список факультетов или найти по названию."""
    count, results = await faculty.get_all(session, page=page, name=name)
    return await get_result(request, count, page, results)


@router.get("/faculty/{pk}/", response_model=FacultyOut, status_code=S.HTTP_200_OK)
async def get_faculty(pk: int, session: AsyncSession = SESSION) -> JSONResponse:
    """Получить факультет по id."""
    return await faculty.get_one(session, pk=pk)


@router.post("/curriculum/", response_model=CurriculumOut, status_code=S.HTTP_201_CREATED)
async def create_curriculum(
    data: CurriculumCreate, session: AsyncSession = SESSION
) -> JSONResponse:
    """Создать учебный план для факультета."""
    return await curriculum.create(session, data.dict())


@router.get("/curriculum/", response_model=Result[CurriculumOut], status_code=S.HTTP_200_OK)
async def get_list_curriculum(
    request: Request,
    page: int = Query(1, ge=1, description="Page offset"),
    name: str = Query(None),
    session: AsyncSession = SESSION,
) -> JSONResponse:
    """Получить список учебных планов или найти по названию."""
    count, results = await curriculum.get_all(session, page=page, name=name)
    return await get_result(request, count, page, results)


@router.get("/curriculum/{pk}/", response_model=CurriculumOut, status_code=S.HTTP_200_OK)
async def get_curriculum(pk: int, session: AsyncSession = SESSION) -> JSONResponse:
    """Получить учебный план по id."""
    return await curriculum.get_one(session, pk=pk)


@router.post("/semester/", response_model=SemesterOut, status_code=S.HTTP_201_CREATED)
async def create_semester(data: SemesterCreate, session: AsyncSession = SESSION) -> JSONResponse:
    """Создать семестр для учебного плана."""
    return await semester.create(session, data.dict())


@router.get("/semester/{pk}/", response_model=SemesterOut, status_code=S.HTTP_200_OK)
async def get_semester(pk: int, session: AsyncSession = SESSION) -> JSONResponse:
    """Получить семестр по id."""
    return await semester.get_one(session, pk=pk)
