from fastapi import APIRouter

from app.api.api_v1.endpoints import country_list
from app.api.api_v1.endpoints import root

api_router = APIRouter()
api_router.include_router(root.router, tags=["root"])
api_router.include_router(country_list.router, tags=["country-list"])