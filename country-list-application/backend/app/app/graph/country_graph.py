import networkx

from .enums import CountryCode


def initialize_country_graph() -> networkx.Graph:
    """Initializes the simplified country graph.

    Creates a networkx graph from an edge list determined by the
    simplified North America map given in the problem. Each vertex
    in the graph is an instance of the `CountryCode` enum.

    Returns:
        The initialized country graph from the simplified North
        America map.
    """
    edge_list = [
        (CountryCode.CAN, CountryCode.USA),
        (CountryCode.USA, CountryCode.CAN),
        (CountryCode.USA, CountryCode.MEX),
        (CountryCode.MEX, CountryCode.USA),
        (CountryCode.MEX, CountryCode.GTM),
        (CountryCode.MEX, CountryCode.BLZ),
        (CountryCode.BLZ, CountryCode.MEX),
        (CountryCode.BLZ, CountryCode.GTM),
        (CountryCode.GTM, CountryCode.MEX),
        (CountryCode.GTM, CountryCode.BLZ),
        (CountryCode.GTM, CountryCode.SLV),
        (CountryCode.GTM, CountryCode.HND),
        (CountryCode.SLV, CountryCode.GTM),
        (CountryCode.SLV, CountryCode.HND),
        (CountryCode.HND, CountryCode.GTM),
        (CountryCode.HND, CountryCode.SLV),
        (CountryCode.HND, CountryCode.NIC),
        (CountryCode.NIC, CountryCode.HND),
        (CountryCode.NIC, CountryCode.CRI),
        (CountryCode.CRI, CountryCode.NIC),
        (CountryCode.CRI, CountryCode.PAN),
        (CountryCode.PAN, CountryCode.CRI),
    ]
    return networkx.Graph(edge_list)


country_graph = initialize_country_graph()
