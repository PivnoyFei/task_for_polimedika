from fastapi import APIRouter

from application.course.views import router as course_router
from application.schedule.views import router as schedule_router
from application.student.views import router as student_router
from application.teacher.views import router as teacher_router

router = APIRouter()

router.include_router(student_router, prefix="/students", tags=["students"])
router.include_router(course_router, tags=["course"])
router.include_router(teacher_router, prefix="/teachers", tags=["teachers"])
router.include_router(schedule_router, prefix="/schedule", tags=["schedule"])
