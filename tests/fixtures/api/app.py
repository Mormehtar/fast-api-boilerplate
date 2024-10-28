import pytest
from fastapi import FastAPI

from api.server import app


@pytest.fixture
def test_app() -> FastAPI:
    return app


__all__ = ["test_app"]
