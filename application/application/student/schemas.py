from pydantic import BaseModel


class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    description: str
    is_learn: bool
    group_id: int


class UserRegistration:
    pass


class StudentIndependentWorkBD(BaseModel):
    independent_work_id: int
    student_id: int
    is_passed: bool
