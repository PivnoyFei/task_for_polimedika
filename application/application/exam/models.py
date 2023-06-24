from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint

from application.database import Base
from application.models import BaseMixin, TimeStampMixin


class Grade(Base, TimeStampMixin):
    """Оценка за экзамен."""

    __tablename__ = "grade"
    __table_args__ = (UniqueConstraint("student_id", "exam_id", name="unique_student_exam"),)

    id = Column(Integer, primary_key=True)
    grade = Column(String, nullable=False)
    student_id = Column(Integer, ForeignKey("student.id", ondelete="CASCADE"))
    exam_id = Column(Integer, ForeignKey("exam.id", ondelete="CASCADE"))


class Exam(Base, TimeStampMixin, BaseMixin):
    """Экзамен."""

    __tablename__ = "exam"
