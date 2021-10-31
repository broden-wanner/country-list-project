from typing import Any

from fastapi import APIRouter

from app.core.config import settings

router = APIRouter()


@router.get("/")
async def root() -> Any:
    return {'detail': f'This is the root url for the {settings.PROJECT_NAME} API.'}