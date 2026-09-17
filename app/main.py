import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import router as v1_router
from app.config import settings
from app.exceptions import global_exception_handler
from app.logging_config import configure_logging

configure_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Backend API for YuvOps Technologix",
)

app.add_exception_handler(Exception, global_exception_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(v1_router)

@app.get("/")
def root():
    logger.info("Root endpoint requested")

    return {
        "message": "YuvOps API is running",
        "status": "ok",
        "environment": settings.environment,
        "debug": settings.debug,
    }

@app.get("/health")
def health():
    logger.info("Health check requested")

    return {
        "status": "healthy",
    }