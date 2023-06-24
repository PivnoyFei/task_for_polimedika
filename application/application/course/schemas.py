from pydantic import BaseModel

from application.schemas import BaseSchema, PrimaryKeySchema, TimeStampSchema


class CourseCreate(BaseModel):
    exam_id: int


class CourseOut(TimeStampSchema, CourseCreate, PrimaryKeySchema):
    pass


class CourseProgramCreate(BaseSchema):
    course_id: int


class CourseProgramOut(TimeStampSchema, CourseProgramCreate, PrimaryKeySchema):
    pass


class IndependentWorkCreate(BaseSchema):
    pass


class IndependentWorkOut(TimeStampSchema, IndependentWorkCreate, PrimaryKeySchema):
    pass
