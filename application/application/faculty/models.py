from sqlalchemy.orm import relationship

from application.database import Base
from application.models import BaseMixin, TimeStampMixin


class Faculty(Base, TimeStampMixin, BaseMixin):
    """Факультет."""

    __tablename__ = "faculty"

    curriculum = relationship("Curriculum", backref="faculty_curriculum")
