from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from application.database import Base
from application.models import TimeStampMixin


class Group(Base, TimeStampMixin):
    """Группа."""

    __tablename__ = "group"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    curriculum_id = Column(Integer, ForeignKey("curriculum.id", ondelete="SET NULL"))

    student = relationship("Student")


class Student(Base, TimeStampMixin):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)
    description = Column(String)
    is_learn = Column(Boolean, nullable=False, default=True)
    group_id = Column(Integer, ForeignKey("group.id", ondelete="SET NULL"))

    grade = relationship("Grade")

    @property
    def first_last_name(self):
        return f"{self.first_name} {self.last_name}"


class StudentIndependentWork(Base, TimeStampMixin):
    """Оценка за задание для самостоятельной работы."""

    __tablename__ = "student_independent_work"
    __table_args__ = (
        UniqueConstraint("independent_work_id", "student_id", name="unique_student_work"),
    )

    id = Column(Integer, primary_key=True)
    is_passed = Column(Boolean, nullable=False)

    independent_work_id = Column(Integer, ForeignKey("independent_work.id", ondelete="CASCADE"))
    independent_work = relationship("IndependentWork", backref="work")

    student_id = Column(Integer, ForeignKey("student.id", ondelete="CASCADE"))
    student = relationship("Student", backref="work")
