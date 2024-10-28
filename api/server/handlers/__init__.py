from fastapi import APIRouter
from .dignostic import diagnostic_router


base_router = APIRouter()
base_router.include_router(diagnostic_router, prefix="/diagnostic")


__all__ = ["base_router"]
