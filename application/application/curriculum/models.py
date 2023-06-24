from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from application.database import Base
from application.models import BaseMixin, TimeStampMixin


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
