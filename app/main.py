import logging
import os

from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator


APP_NAME = os.getenv("APP_NAME", "fastapi-k8s-app")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
ENABLE_DOCS = os.getenv("ENABLE_DOCS", "true").lower() == "true"
APP_ENV = os.getenv("APP_ENV", "development").lower()
APP_SECRET_KEY = os.getenv("APP_SECRET_KEY", "")

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
)
logger = logging.getLogger(APP_NAME)

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    docs_url="/docs" if ENABLE_DOCS else None,
    redoc_url="/redoc" if ENABLE_DOCS else None,
)

Instrumentator(
    should_group_status_codes=False,
    should_ignore_untemplated=True,
    should_respect_env_var=False,
).instrument(app).expose(app, endpoint="/metrics", include_in_schema=False)


@app.get("/", tags=["default"])
def read_root() -> dict[str, str]:
    logger.info("Root endpoint requested")
    return {
        "message": "FastAPI application is running",
        "app": APP_NAME,
        "version": APP_VERSION,
    }


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "app": APP_NAME,
        "version": APP_VERSION,
    }


@app.get("/livez", tags=["health"])
def live() -> dict[str, str]:
    return {"status": "alive"}


@app.get("/readyz", tags=["health"])
def ready() -> dict[str, str]:
    if APP_ENV == "production" and not APP_SECRET_KEY:
        raise HTTPException(status_code=503, detail="Required secret is missing")
    return {"status": "ready"}
