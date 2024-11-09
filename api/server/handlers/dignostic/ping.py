from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing_extensions import Annotated
from api.dependencies.settings import get_app_settings
from settings.app import AppSettings

ping_router = APIRouter()


class PingResponse(BaseModel):
    environment: str
    status: str = "ok"


@ping_router.get("/ping")
async def ping(app_settings: Annotated[AppSettings, Depends(get_app_settings)]) -> PingResponse:
    return PingResponse(
        environment=app_settings.environment,
    )
