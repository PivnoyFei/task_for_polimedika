from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table, Text
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

# Assoc table for Course and Semester
course_semester = Table(
    "course_semester",
    Base.metadata,
    Column("course_id", Integer, ForeignKey("course.id", ondelete="CASCADE")),
    Column("semester_id", Integer, ForeignKey("semester.id", ondelete="CASCADE")),
    # PrimaryKeyConstraint("course_id", "semester_id"),
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


class Exam(Base, TimeStampMixin, BaseMixin):
    """Экзамен."""

    __tablename__ = "exam"


class Faculty(Base, TimeStampMixin, BaseMixin):
    """Факультет."""

    __tablename__ = "faculty"

    curriculum = relationship("Curriculum", backref="faculty_curriculum")


class Curriculum(Base, TimeStampMixin, BaseMixin):
    """
    Учебный план.
    У каждого факультета несколько учебных планов.
    """

    __tablename__ = "curriculum"

    start_at = Column(DateTime, nullable=False)
    end_at = Column(DateTime, nullable=False)
    faculty_id = Column(Integer, ForeignKey("faculty.id", ondelete="SET NULL"))

    group = relationship("Group", backref="curriculum_group")


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


class Course(Base, TimeStampMixin, BaseMixin):
    """Курс."""

    __tablename__ = "course"

    exam_id = Column(Integer, ForeignKey("exam.id", ondelete="SET NULL"))

    semester = relationship(
        "Semester",
        secondary=course_semester,
        back_populates="course",
    )
