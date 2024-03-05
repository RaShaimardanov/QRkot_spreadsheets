from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_charityproject_id_by_name(
            self,
            charityproject: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_charityproject_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == charityproject
            )
        )
        return db_charityproject_id.scalars().first()

    async def get_next_charityproject_not_fully_invested(
            self,
            session: AsyncSession,
    ) -> CharityProject:
        db_charityproject = await session.execute(
            select(CharityProject).where(
                ~CharityProject.fully_invested
            ).order_by(CharityProject.create_date.asc())
        )
        return db_charityproject.scalars().first()

    async def get_projects_fully_invested(
            self,
            session: AsyncSession,
    ) -> list[CharityProject]:
        db_charityprojects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested
            )
        )
        return db_charityprojects.scalars().all()

    async def get_projects_by_completion_rate(self, session: AsyncSession):
        db_charityprojects = await self.get_projects_fully_invested(session)
        db_charityprojects.sort(key=lambda x: x.get_spent_time)
        return db_charityprojects


charityproject_crud = CRUDCharityProject(CharityProject)
