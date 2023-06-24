from fastapi import APIRouter, Depends
from fastapi import status as S
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from application.database import db_session
from application.managers import Managers
from application.semester.managers import SemesterManagers
from application.semester.models import Semester
from application.semester.schemas import SemesterCreate, SemesterOut
from application.settings import DELETE_RESPONSES as DEL_RESP
from application.settings import GET_RESPONSES as GET_RESP

router = APIRouter()
SESSION: AsyncSession = Depends(db_session)
semester = Managers(Semester)


@router.post("/", response_model=SemesterOut, status_code=S.HTTP_201_CREATED)
async def create_semester(data: SemesterCreate, session: AsyncSession = SESSION) -> JSONResponse:
    """Создать семестр для учебного плана."""
    if not await SemesterManagers.check_name_year(session, data):
        return await semester.create(session, data.dict())
    return JSONResponse({"detail": "Такой семестр уже существует"}, S.HTTP_400_BAD_REQUEST)


@router.get("/{pk}/", response_model=SemesterOut, status_code=S.HTTP_200_OK, responses=GET_RESP)
async def get_semester(pk: int, session: AsyncSession = SESSION) -> JSONResponse:
    """Получить семестр по id."""
    return await semester.get_one(session, pk=pk)


@router.delete("/{pk}/", response_model=None, status_code=S.HTTP_204_NO_CONTENT, responses=DEL_RESP)
async def delete_semester(pk: int, session: AsyncSession = SESSION) -> JSONResponse:
    """Удалить семестр по id."""
    if not await semester.delete(session, pk=pk):
        return JSONResponse({"detail": "Семестр не существует"}, S.HTTP_404_NOT_FOUND)
