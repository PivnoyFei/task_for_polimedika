from fastapi import APIRouter, Depends, Request
from fastapi import status as S
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from application.database import db_session
from application.exam.models import Exam
from application.exam.schemas import ExamCreate, ExamOut
from application.managers import Managers
from application.schemas import Result, SearchName
from application.services import get_result
from application.settings import DELETE_RESPONSES as DEL_RESP
from application.settings import GET_RESPONSES as GET_RESP

router = APIRouter()
SESSION: AsyncSession = Depends(db_session)
exam = Managers(Exam)


@router.post("/", response_model=ExamOut, status_code=S.HTTP_201_CREATED)
async def create_exam(data: ExamCreate, session: AsyncSession = SESSION) -> JSONResponse:
    """Создать экзамен."""
    return await exam.create(session, data.dict())


@router.get("/", response_model=Result[ExamOut], status_code=S.HTTP_200_OK)
async def get_exams(
    request: Request,
    params: SearchName = Depends(),
    session: AsyncSession = SESSION,
) -> JSONResponse:
    """Получить список экзаменов или найти по названию."""
    count, results = await exam.get_all(session, params, attr_name="name")
    return await get_result(request, count, params, results)


@router.get("/{pk}/", response_model=ExamOut, status_code=S.HTTP_200_OK, responses=GET_RESP)
async def get_exam(pk: int, session: AsyncSession = SESSION) -> JSONResponse:
    """Получить экзамен по id."""
    return await exam.get_one(session, pk=pk)


@router.delete("/{pk}/", response_model=None, status_code=S.HTTP_204_NO_CONTENT, responses=DEL_RESP)
async def delete_exam(pk: int, session: AsyncSession = SESSION) -> JSONResponse:
    """Удалить экзамен по id."""
    if not await exam.delete(session, pk=pk):
        return JSONResponse({"detail": "Экзамен не существует"}, S.HTTP_404_NOT_FOUND)
