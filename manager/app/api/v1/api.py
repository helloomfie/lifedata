from fastapi import APIRouter

from app.api.v1.routes.health import router as health_router
from app.api.v1.routes.people import router as people_router

api_router = APIRouter()
api_router.include_router(health_router)
api_router.include_router(people_router)
