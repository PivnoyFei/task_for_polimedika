from fastapi import APIRouter, Depends, Request
from fastapi import status as S
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from application.course.models import Course
from application.course.schemas import CourseCreate, CourseOut
from application.database import db_session
from application.managers import Managers
from application.schemas import Result, SearchName
from application.services import get_result
from application.settings import DELETE_RESPONSES as DEL_RESP
from application.settings import GET_RESPONSES as GET_RESP

router = APIRouter()
SESSION: AsyncSession = Depends(db_session)
course = Managers(Course)


@router.post("/", response_model=CourseOut, status_code=S.HTTP_201_CREATED)
async def create_course(data: CourseCreate, session: AsyncSession = SESSION) -> JSONResponse:
    """Создать курс."""
    return await course.create(session, data.dict())


@router.get("/", response_model=Result[CourseOut], status_code=S.HTTP_200_OK)
async def get_courses(
    request: Request,
    params: SearchName = Depends(),
    session: AsyncSession = SESSION,
) -> JSONResponse:
    """Получить список курсов или найти по названию."""
    count, results = await course.get_all(session, params, attr_name="name")
    return await get_result(request, count, params, results)


@router.get("/{pk}/", response_model=CourseOut, status_code=S.HTTP_200_OK, responses=GET_RESP)
async def get_course(pk: int, session: AsyncSession = SESSION) -> JSONResponse:
    """Получить курс по id."""
    return await course.get_one(session, pk=pk)


@router.delete("/{pk}/", response_model=None, status_code=S.HTTP_204_NO_CONTENT, responses=DEL_RESP)
async def delete_course(pk: int, session: AsyncSession = SESSION) -> JSONResponse:
    """Удалить семестр по id."""
    if not await course.delete(session, pk=pk):
        return JSONResponse({"detail": "Курс не существует"}, S.HTTP_404_NOT_FOUND)
