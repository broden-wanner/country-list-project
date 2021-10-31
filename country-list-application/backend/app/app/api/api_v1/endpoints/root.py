from typing import Any

from fastapi import APIRouter

from app.core.config import settings
from app.schemas import MessageSchema

router = APIRouter()


@router.get("/", response_model=MessageSchema)
async def root() -> Any:
    """Returns a simple message for the root of the project"""
    return {"detail": f"This is the root url for the {settings.PROJECT_NAME} API."}
