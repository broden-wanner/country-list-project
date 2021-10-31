from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.get("/{country_code}")
async def read_items(country_code: str) -> Any:
    return {'detail': country_code}