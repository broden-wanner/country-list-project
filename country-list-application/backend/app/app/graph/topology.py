import networkx

from .country_graph import country_graph
from .enums import CountryCode


def shortest_path_between_countries(
    source: CountryCode, target: CountryCode
) -> list[CountryCode]:
    """Finds the shortest path between two countries using the country graph and
    Dijkstra's algorithm.

    Args:
        source: The country code of the starting country.
        target: The country code of the country we want to travel to.

    Returns:
        The shortest path of countries to travel through in order to go from the
        source to the target country.
    """
    path = networkx.shortest_path(
        country_graph, source=source, target=target, method="dijkstra"
    )
    return path
