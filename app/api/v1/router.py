from fastapi import APIRouter

from app.config import settings

router = APIRouter(
    prefix="/api/v1",
)


@router.get("/status")
def api_status():
    return {
        "service": settings.app_name,
        "version": "v1",
        "status": "operational",
    }


@router.get("/info")
def api_info():
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
    }