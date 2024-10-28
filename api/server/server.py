from fastapi import FastAPI
from .handlers import base_router

app = FastAPI()
app.include_router(base_router)


__all__ = ["app"]
