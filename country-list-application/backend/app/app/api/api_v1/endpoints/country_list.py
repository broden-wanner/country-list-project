from typing import Any

from fastapi import APIRouter

import networkx as nx

router = APIRouter()


@router.get("/{country_code}")
async def get_country_list(country_code: str) -> Any:
    edge_list = [
        ("CAN", "USA"),
        ("USA", "CAN"),
        ("USA", "MEX"),
        ("MEX", "USA"),
        ("MEX", "GTM"),
        ("MEX", "BLZ"),
        ("BLZ", "MEX"),
        ("BLZ", "GTM"),
        ("GTM", "MEX"),
        ("GTM", "BLZ"),
        ("GTM", "SLV"),
        ("GTM", "HND"),
        ("SLV", "GTM"),
        ("SLV", "HND"),
        ("HND", "GTM"),
        ("HND", "SLV"),
        ("HND", "NIC"),
        ("NIC", "HND"),
        ("NIC", "CRI"),
        ("CRI", "NIC"),
        ("CRI", "PAN"),
        ("PAN", "CRI"),
    ]
    G = nx.Graph(edge_list)
    path = nx.shortest_path(G, source="USA", target=country_code)
    return {'detail': path}