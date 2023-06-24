from datetime import datetime

from pydantic import root_validator

from application.schemas import BaseSchema, PrimaryKeySchema, TimeStampSchema


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


class CurriculumOut(TimeStampSchema, BaseSchema, PrimaryKeySchema):
    start_at: datetime
    end_at: datetime
    faculty_id: int
