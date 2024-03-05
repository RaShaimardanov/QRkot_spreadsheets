from aiogoogle import Aiogoogle

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import charityproject_crud
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.core.google_client import get_service
from app.schemas.charityproject import CharityProjectDB
from app.services.google_api import (
    spreadsheets_update_value, set_user_permissions, spreadsheets_create
)


router = APIRouter()


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    dependencies=[Depends(current_superuser)],

)
async def get_all_charity_project(
        session: AsyncSession = Depends(get_async_session),
        wrapper_services: Aiogoogle = Depends(get_service)
):
    """Получить список всех проектов."""
    projects = await charityproject_crud.get_projects_by_completion_rate(session)
    spreadsheetid = await spreadsheets_create(wrapper_services)
    await set_user_permissions(spreadsheetid, wrapper_services)
    await spreadsheets_update_value(spreadsheetid,
                                    projects,
                                    wrapper_services)
    return projects
