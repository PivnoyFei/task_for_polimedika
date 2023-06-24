from datetime import datetime
from typing import Generic, TypeVar

from fastapi import Query
from pydantic import AnyUrl, BaseModel, Field
from pydantic.generics import GenericModel

from application.settings import PAGINATION_SIZE

M = TypeVar("M", bound=BaseModel)


class PrimaryKeySchema(BaseModel):
    id: int


class BaseSchema(BaseModel):
    name: str = Field(min_length=1, max_length=128)
    description: str


class Result(GenericModel, Generic[M]):
    count: int
    next: AnyUrl = None
    previous: AnyUrl = None
    results: list[M]


class TimeStampSchema(BaseModel):
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        orm_mode = True
        validate_assignment = True
        arbitrary_types_allowed = True
        anystr_strip_whitespace = True


class Params(BaseModel):
    page: int = Query(1, ge=1, description="Номер страницы")
    limit: int = Query(PAGINATION_SIZE, ge=1, le=100, description="Ограничение страницы")


class SearchName(Params):
    name: str = Query(None, max_length=128, description="Поиск по имени")
