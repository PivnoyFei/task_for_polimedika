from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import func

from application.course.models import Curriculum, Faculty
from application.course.schemas import FacultyCreate, FacultyOut
from application.managers import Managers
from application.services import limit_offset


class FacultyManagers:
    pass
