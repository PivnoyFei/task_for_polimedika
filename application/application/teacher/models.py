from sqlalchemy import Column, ForeignKey, Integer, PrimaryKeyConstraint, String, Table
from sqlalchemy.orm import relationship

from application.database import Base
from application.models import TimeStampMixin

# Assoc table for building and teacher
building_teacher = Table(
    "building_teacher",
    Base.metadata,
    Column("teacher_id", Integer, ForeignKey("teacher.id", ondelete="CASCADE")),
    Column("building_id", Integer, ForeignKey("building.id", ondelete="CASCADE")),
    # PrimaryKeyConstraint('teacher_id', 'building_id'),
)

# Assoc table for course and teacher
course_teacher = Table(
    "course_teacher",
    Base.metadata,
    Column("teacher_id", Integer, ForeignKey("teacher.id", ondelete="CASCADE")),
    Column("course_id", Integer, ForeignKey("course.id", ondelete="CASCADE")),
    # PrimaryKeyConstraint("teacher_id", "course_id"),
)


class Teacher(Base, TimeStampMixin):
    __tablename__ = "teacher"

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)

    building = relationship(
        "Building",
        secondary=building_teacher,
        backref="teacher",
    )
    course = relationship(
        "Course",
        secondary=course_teacher,
        backref="teacher",
    )
