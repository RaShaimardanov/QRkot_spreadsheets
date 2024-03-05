from datetime import timedelta

from sqlalchemy import Column, String, Text
from sqlalchemy.ext.hybrid import hybrid_property

from app.core.db import Base
from app.models.base import BaseModelMixin


class CharityProject(BaseModelMixin, Base):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)

    @hybrid_property
    def get_spent_time(self) -> timedelta:
        return self.close_date - self.create_date
