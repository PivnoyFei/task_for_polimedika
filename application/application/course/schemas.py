from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import Form
from pydantic import BaseModel, Field, root_validator, validator

from application.schemas import BaseSchema, TimeStampSchema


class FacultyCreate(BaseSchema):
    pass


class FacultyOut(TimeStampSchema, FacultyCreate):
    pass


class CurriculumCreate(BaseSchema):
    start_at: datetime
    end_at: datetime
    faculty_id: int

    @root_validator()
    def check_date_range(cls, values: dict) -> dict:
        start_at: datetime = values["start_at"]
        end_at: datetime = values["end_at"]

        if start_at > end_at:
            raise ValueError("Дата окончания не может быть раньше даты начала")

        if datetime.utcnow() >= start_at:
            raise ValueError("Дата не должна быть задним числом")

        return values


class CurriculumOut(TimeStampSchema, BaseSchema):
    start_at: datetime
    end_at: datetime
    faculty_id: int


class SemesterCreate(BaseModel):
    num: int
    year: int
    curriculum_id: int


class SemesterOut(TimeStampSchema, SemesterCreate):
    pass


class CourseCreate(BaseModel):
    exam_id: int


class CourseOut(TimeStampSchema, CourseCreate):
    pass


class CourseProgramCreate(BaseSchema):
    course_id: int


class CourseProgramOut(TimeStampSchema, CourseProgramCreate):
    pass


class IndependentWorkCreate(BaseSchema):
    pass


class IndependentWorkOut(TimeStampSchema, IndependentWorkCreate):
    pass


class ExamCreate(BaseSchema):
    pass


class ExamOut(TimeStampSchema, ExamCreate):
    pass
