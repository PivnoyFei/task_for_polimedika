from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from application.database import Base
from application.models import TimeStampMixin


class Building(Base, TimeStampMixin):
    """Дом."""

    __tablename__ = "building"

    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False)

    building = relationship(
        "Teacher",
        secondary="building_teacher",
        back_populates="building",
    )


class Branch(Base, TimeStampMixin):
    """Отделение."""

    __tablename__ = "branch"

    id = Column(Integer, primary_key=True)
    num = Column(Integer, nullable=False)
    building_id = Column(Integer, ForeignKey("building.id", ondelete="CASCADE"))


class Audience(Base, TimeStampMixin):
    """Аудитория."""

    __tablename__ = "audience"

    id = Column(Integer, primary_key=True)
    num = Column(Integer, nullable=False)
    building_id = Column(Integer, ForeignKey("building.id", ondelete="CASCADE"))
    branch_id = Column(Integer, ForeignKey("branch.id", ondelete="CASCADE"))


class Schedule(Base, TimeStampMixin):
    """Расписание"""

    __tablename__ = "schedule"

    id = Column(Integer, primary_key=True)
    start_at = Column(DateTime, nullable=False)
    end_at = Column(DateTime, nullable=False)
    group_id = Column(Integer, ForeignKey("group.id", ondelete="CASCADE"))
    building_id = Column(Integer, ForeignKey("building.id", ondelete="CASCADE"))
    branch_id = Column(Integer, ForeignKey("branch.id", ondelete="CASCADE"))
    audience_id = Column(Integer, ForeignKey("audience.id", ondelete="CASCADE"))
    exam_id = Column(Integer, ForeignKey("exam.id", ondelete="CASCADE"))
