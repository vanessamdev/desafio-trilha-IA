"""
FastAPI Application Entry Point
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.core.config import get_settings
from backend.app.presentation.routes import health_router, document_router, image_router
from backend.app.presentation.routes.contract_routes import router as contract_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler"""
    # Startup
    yield
    # Shutdown


def create_app() -> FastAPI:
    """Application factory"""
    settings = get_settings()
    
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan
    )
    
    configure_middleware(app, settings)
    configure_routes(app)
    
    return app


def configure_middleware(app: FastAPI, settings) -> None:
    """Configure application middleware"""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def configure_routes(app: FastAPI) -> None:
    """Configure application routes"""
    app.include_router(health_router, prefix="/api/v1", tags=["Health"])
    app.include_router(document_router, prefix="/api/v1/documents", tags=["Documents"])
    app.include_router(image_router, prefix="/api/v1/images", tags=["Images"])
    app.include_router(contract_router, prefix="/api/v1", tags=["Contracts"])


app = create_app()
