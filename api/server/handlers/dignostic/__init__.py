from fastapi import APIRouter

from .ping import ping_router


diagnostic_router = APIRouter(tags=["diagnostic"])
diagnostic_router.include_router(ping_router)


__all__ = ["diagnostic_router"]
