from fastapi import APIRouter, Depends, Request
from fastapi import status as S
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from application.curriculum.models import Curriculum
from application.curriculum.schemas import CurriculumCreate, CurriculumOut
from application.database import db_session
from application.managers import Managers
from application.schemas import Result, SearchName
from application.services import get_result
from application.settings import DELETE_RESPONSES, GET_RESPONSES

router = APIRouter()
SESSION: AsyncSession = Depends(db_session)
curriculum = Managers(Curriculum)


@router.post("/", response_model=CurriculumOut, status_code=S.HTTP_201_CREATED)
async def create_curriculum(
    data: CurriculumCreate, session: AsyncSession = SESSION
) -> JSONResponse:
    """Создать учебный план для факультета."""
    return await curriculum.create(session, data.dict())


@router.get("/", response_model=Result[CurriculumOut], status_code=S.HTTP_200_OK)
async def get_list_curriculum(
    request: Request,
    params: SearchName = Depends(),
    session: AsyncSession = SESSION,
) -> JSONResponse:
    """Получить список учебных планов или найти по названию."""
    count, results = await curriculum.get_all(session, params, attr_name="name")
    return await get_result(request, count, params, results)


@router.get(
    "/{pk}/",
    response_model=CurriculumOut,
    status_code=S.HTTP_200_OK,
    responses=GET_RESPONSES,
)
async def get_curriculum(pk: int, session: AsyncSession = SESSION) -> JSONResponse:
    """Получить учебный план по id."""
    return await curriculum.get_one(session, pk=pk)


@router.delete(
    "/{pk}/",
    response_model=None,
    status_code=S.HTTP_204_NO_CONTENT,
    responses=DELETE_RESPONSES,
)
async def delete_curriculum(pk: int, session: AsyncSession = SESSION) -> JSONResponse:
    """Удалить семестр по id."""
    if not await curriculum.delete(session, pk=pk):
        return JSONResponse({"detail": "Учебный план не существует"}, S.HTTP_404_NOT_FOUND)
