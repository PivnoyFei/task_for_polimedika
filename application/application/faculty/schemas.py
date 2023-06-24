from application.schemas import BaseSchema, PrimaryKeySchema, TimeStampSchema


class FacultyCreate(BaseSchema):
    pass


class FacultyOut(TimeStampSchema, FacultyCreate, PrimaryKeySchema):
    pass
