from fastapi import APIRouter
from pydantic import BaseModel

ping_router = APIRouter()


class PingResponse(BaseModel):
    status: str = "ok"


@ping_router.get("/ping")
async def ping() -> PingResponse:
    return PingResponse()
