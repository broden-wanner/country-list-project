from fastapi.testclient import TestClient

from app.core.config import settings


def test_get_root(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}")
    assert response.status_code == 200
    content = response.json()
    assert (
        content["detail"]
        == f"This is the root url for the {settings.PROJECT_NAME} API."
    )
