from datetime import datetime
from typing import Generic, TypeVar

from pydantic import AnyUrl, BaseModel, Field
from pydantic.generics import GenericModel

M = TypeVar("M", bound=BaseModel)


class BaseSchema(BaseModel):
    name: str = Field(min_length=1, max_length=128)
    description: str = Field()


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
