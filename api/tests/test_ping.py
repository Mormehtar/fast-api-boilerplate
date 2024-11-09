import pytest
from httpx import AsyncClient
from starlette.status import HTTP_200_OK
from settings.app import AppSettings


@pytest.mark.anyio
class TestPing:
    async def test_ping(self, test_client: AsyncClient):
        response = await test_client.get("http://test/diagnostic/ping")
        assert response.status_code == HTTP_200_OK
        assert response.json() == {"status": "ok", "environment": AppSettings().environment}
