import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient


@pytest.fixture
async def test_client(test_app: FastAPI) -> AsyncClient:
    async with AsyncClient(transport=ASGITransport(app=test_app), base_url="http://test") as async_client:
        yield async_client


__all__ = ["test_client"]
