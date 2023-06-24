from pydantic import BaseModel

from application.schemas import BaseSchema, PrimaryKeySchema, TimeStampSchema


class ExamCreate(BaseSchema):
    pass


class ExamOut(TimeStampSchema, ExamCreate, PrimaryKeySchema):
    pass


class GradeCreate(BaseModel):
    grade: str
    student_id: int
    exam_id: int


class GradeOut(TimeStampSchema, GradeCreate, PrimaryKeySchema):
    pass
