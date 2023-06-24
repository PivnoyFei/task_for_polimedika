from typing import Any

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from application.database import db_session
from application.student.managers import create, get_student
from application.student.models import Student
from application.student.schemas import StudentCreate

router = APIRouter()
