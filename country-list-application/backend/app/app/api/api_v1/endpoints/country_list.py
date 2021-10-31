from typing import Any
from fastapi import APIRouter
from app.schemas import CountryListSchema
from app.graph.enums import CountryCode
from app.graph.topology import shortest_path_between_countries


router = APIRouter()

@router.get("/{destination_country_code}", response_model=CountryListSchema)
async def get_country_list(destination_country_code: CountryCode) -> Any:
    """Returns the path to travel from the USA to the given country code.
    Uses the country graph to find the shortest path between USA and the 
    country code passed in as a path parameter.
    """
    path = shortest_path_between_countries(source=CountryCode.USA, target=destination_country_code)
    return {
        'destination': destination_country_code, 
        'list': path
    }