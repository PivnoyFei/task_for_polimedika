from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship

from application.database import Base
from application.models import BaseMixin, TimeStampMixin

# Assoc table for IndependentWork and CourseProgram
course_program_independent_work = Table(
    "course_program_independent_work",
    Base.metadata,
    Column(
        "independent_work_id",
        Integer,
        ForeignKey("independent_work.id", ondelete="CASCADE"),
    ),
    Column(
        "course_program_id",
        Integer,
        ForeignKey("course_program.id", ondelete="CASCADE"),
    ),
    # PrimaryKeyConstraint("independent_work_id", "course_program_id"),
)


class IndependentWork(Base, TimeStampMixin, BaseMixin):
    """Задание для самостоятельной работы."""

    __tablename__ = "independent_work"

    course_program = relationship(
        "CourseProgram",
        secondary=course_program_independent_work,
        back_populates="independent_work",
    )


class CourseProgram(Base, TimeStampMixin, BaseMixin):
    """
    Программа курса, у одного курса может быть несколько програм обучения
    у каждой программы несколько домашних работ.
    """

    __tablename__ = "course_program"

    course_id = Column(Integer, ForeignKey("course.id", ondelete="SET NULL"))

    independent_work = relationship(
        "IndependentWork",
        secondary=course_program_independent_work,
        back_populates="course_program",
    )


class Course(Base, TimeStampMixin, BaseMixin):
    """Курс."""

    __tablename__ = "course"

    exam_id = Column(Integer, ForeignKey("exam.id", ondelete="SET NULL"))

    semester = relationship(
        "Semester",
        secondary="course_semester",
        back_populates="course",
    )
