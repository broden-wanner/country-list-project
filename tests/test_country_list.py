import requests

API_ROOT_URL = "https://countrylist.brodenwanner.com"


def test_get_country_list_to_panama() -> None:
    response = requests.get(f"{API_ROOT_URL}/PAN")
    assert response.status_code == 200
    content = response.json()
    assert content["destination"] == "PAN"
    assert content["list"] == ["USA", "MEX", "GTM", "HND", "NIC", "CRI", "PAN"]


def test_get_country_list_invalid_code() -> None:
    response = requests.get(f"{API_ROOT_URL}/not-a-code")
    assert response.status_code == 422
    content = response.json()["detail"][0]
    assert (
        content["msg"]
        == "value is not a valid enumeration member; permitted: 'CAN', 'USA', "
        + "'MEX', 'BLZ', 'GTM', 'SLV', 'HND', 'NIC', 'CRI', 'PAN'"
    )
    assert content["type"] == "type_error.enum"


def test_get_country_list_to_us() -> None:
    response = requests.get(f"{API_ROOT_URL}/USA")
    assert response.status_code == 200
    content = response.json()
    assert content["destination"] == "USA"
    assert content["list"] == ["USA"]


def test_get_country_list_to_canada() -> None:
    response = requests.get(f"{API_ROOT_URL}/CAN")
    assert response.status_code == 200
    content = response.json()
    assert content["destination"] == "CAN"
    assert content["list"] == ["USA", "CAN"]


def test_get_country_list_to_belize() -> None:
    response = requests.get(f"{API_ROOT_URL}/BLZ")
    assert response.status_code == 200
    content = response.json()
    assert content["destination"] == "BLZ"
    assert content["list"] == ["USA", "MEX", "BLZ"]


def test_get_country_list_to_guatemala() -> None:
    response = requests.get(f"{API_ROOT_URL}/GTM")
    assert response.status_code == 200
    content = response.json()
    assert content["destination"] == "GTM"
    assert content["list"] == ["USA", "MEX", "GTM"]


def test_get_country_list_to_el_salvador() -> None:
    response = requests.get(f"{API_ROOT_URL}/SLV")
    assert response.status_code == 200
    content = response.json()
    assert content["destination"] == "SLV"
    assert content["list"] == ["USA", "MEX", "GTM", "SLV"]


def test_get_country_list_to_honduras() -> None:
    response = requests.get(f"{API_ROOT_URL}/HND")
    assert response.status_code == 200
    content = response.json()
    assert content["destination"] == "HND"
    assert content["list"] == ["USA", "MEX", "GTM", "HND"]


def test_get_country_list_to_nicaragua() -> None:
    response = requests.get(f"{API_ROOT_URL}/NIC")
    assert response.status_code == 200
    content = response.json()
    assert content["destination"] == "NIC"
    assert content["list"] == ["USA", "MEX", "GTM", "HND", "NIC"]


def test_get_country_list_to_costa_rica() -> None:
    response = requests.get(f"{API_ROOT_URL}/CRI")
    assert response.status_code == 200
    content = response.json()
    assert content["destination"] == "CRI"
    assert content["list"] == ["USA", "MEX", "GTM", "HND", "NIC", "CRI"]
