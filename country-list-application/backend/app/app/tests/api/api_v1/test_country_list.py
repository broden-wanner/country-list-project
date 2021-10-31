from fastapi.testclient import TestClient

from app.core.config import settings


def test_get_country_list_to_panama(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}/PAN")
    assert response.status_code == 200
    content = response.json()
    assert content["destination"] == "PAN"
    assert content["list"] == ["USA", "MEX", "GTM", "HND", "NIC", "CRI", "PAN"]


def test_get_country_list_invalid_code(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}/not-a-code")
    assert response.status_code == 422
    content = response.json()["detail"][0]
    assert (
        content["msg"]
        == "value is not a valid enumeration member; permitted: 'CAN', 'USA', "
        + "'MEX', 'BLZ', 'GTM', 'SLV', 'HND', 'NIC', 'CRI', 'PAN'"
    )
    assert content["type"] == "type_error.enum"


def test_get_country_list_to_us(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}/USA")
    assert response.status_code == 200
    content = response.json()
    assert content["destination"] == "USA"
    assert content["list"] == ["USA"]


def test_get_country_list_to_canada(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}/CAN")
    assert response.status_code == 200
    content = response.json()
    assert content["destination"] == "CAN"
    assert content["list"] == ["USA", "CAN"]


def test_get_country_list_to_belize(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}/BLZ")
    assert response.status_code == 200
    content = response.json()
    assert content["destination"] == "BLZ"
    assert content["list"] == ["USA", "MEX", "BLZ"]


def test_get_country_list_to_guatemala(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}/GTM")
    assert response.status_code == 200
    content = response.json()
    assert content["destination"] == "GTM"
    assert content["list"] == ["USA", "MEX", "GTM"]


def test_get_country_list_to_el_salvador(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}/SLV")
    assert response.status_code == 200
    content = response.json()
    assert content["destination"] == "SLV"
    assert content["list"] == ["USA", "MEX", "GTM", "SLV"]


def test_get_country_list_to_honduras(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}/HND")
    assert response.status_code == 200
    content = response.json()
    assert content["destination"] == "HND"
    assert content["list"] == ["USA", "MEX", "GTM", "HND"]


def test_get_country_list_to_nicaragua(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}/NIC")
    assert response.status_code == 200
    content = response.json()
    assert content["destination"] == "NIC"
    assert content["list"] == ["USA", "MEX", "GTM", "HND", "NIC"]


def test_get_country_list_to_costa_rica(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}/CRI")
    assert response.status_code == 200
    content = response.json()
    assert content["destination"] == "CRI"
    assert content["list"] == ["USA", "MEX", "GTM", "HND", "NIC", "CRI"]
