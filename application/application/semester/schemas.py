from pydantic import BaseModel

from application.schemas import PrimaryKeySchema, TimeStampSchema


class SemesterCreate(BaseModel):
    num: int
    year: int
    curriculum_id: int


class SemesterOut(TimeStampSchema, SemesterCreate, PrimaryKeySchema):
    pass
