from fastapi import APIRouter, Depends, Request
from fastapi import status as S
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from application.database import db_session
from application.faculty.models import Faculty
from application.faculty.schemas import FacultyCreate, FacultyOut
from application.managers import Managers
from application.schemas import Result, SearchName
from application.services import get_result
from application.settings import DELETE_RESPONSES as DEL_RESP
from application.settings import GET_RESPONSES as GET_RESP

router = APIRouter()
SESSION: AsyncSession = Depends(db_session)
faculty = Managers(Faculty)


@router.post("/", response_model=FacultyOut, status_code=S.HTTP_201_CREATED)
async def create_faculty(data: FacultyCreate, session: AsyncSession = SESSION) -> JSONResponse:
    """Создать факультет."""
    return await faculty.create(session, data.dict())


@router.get("/", response_model=Result[FacultyOut], status_code=S.HTTP_200_OK)
async def get_faculties(
    request: Request,
    params: SearchName = Depends(),
    session: AsyncSession = SESSION,
) -> JSONResponse:
    """Получить список факультетов или найти по названию."""
    count, results = await faculty.get_all(session, params, attr_name="name")
    return await get_result(request, count, params, results)


@router.get("/{pk}/", response_model=FacultyOut, status_code=S.HTTP_200_OK, responses=GET_RESP)
async def get_faculty(pk: int, session: AsyncSession = SESSION) -> JSONResponse:
    """Получить факультет по id."""
    return await faculty.get_one(session, pk=pk)


@router.delete("/{pk}/", response_model=None, status_code=S.HTTP_204_NO_CONTENT, responses=DEL_RESP)
async def delete_faculty(pk: int, session: AsyncSession = SESSION) -> JSONResponse:
    """Удалить факультет по id."""
    if not await faculty.delete(session, pk=pk):
        return JSONResponse({"detail": "Факультет не существует"}, S.HTTP_404_NOT_FOUND)
