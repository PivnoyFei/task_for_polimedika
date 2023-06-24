from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship

from application.database import Base
from application.models import TimeStampMixin

# Assoc table for Course and Semester
course_semester = Table(
    "course_semester",
    Base.metadata,
    Column("course_id", Integer, ForeignKey("course.id", ondelete="CASCADE")),
    Column("semester_id", Integer, ForeignKey("semester.id", ondelete="CASCADE")),
    # PrimaryKeyConstraint("course_id", "semester_id"),
)


class Semester(Base, TimeStampMixin):
    """Семестр."""

    __tablename__ = "semester"

    id = Column(Integer, primary_key=True)
    num = Column(Integer, nullable=False)
    year = Column(Integer, default=datetime.now().date().year)
    curriculum_id = Column(Integer, ForeignKey("curriculum.id", ondelete="SET NULL"))

    course = relationship(
        "Course",
        secondary=course_semester,
        back_populates="semester",
    )
