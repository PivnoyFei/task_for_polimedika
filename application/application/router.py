from fastapi import APIRouter

from application.course.views import router as course_router
from application.curriculum.views import router as curriculum_router
from application.exam.views import router as exam_router
from application.faculty.views import router as faculty_router
from application.schedule.views import router as schedule_router
from application.semester.views import router as semester_router
from application.student.views import router as student_router
from application.teacher.views import router as teacher_router

router = APIRouter()

router.include_router(student_router, prefix="/students", tags=["students"])
router.include_router(course_router, prefix="/courses", tags=["course"])
router.include_router(curriculum_router, prefix="/curriculum", tags=["scurriculum"])
router.include_router(exam_router, prefix="/exam", tags=["exam"])
router.include_router(faculty_router, prefix="/faculty", tags=["faculty"])
router.include_router(semester_router, prefix="/semester", tags=["semester"])
router.include_router(teacher_router, prefix="/teachers", tags=["teachers"])
router.include_router(schedule_router, prefix="/schedule", tags=["schedule"])
