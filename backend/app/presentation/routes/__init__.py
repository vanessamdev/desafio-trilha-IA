"""
API Routes
"""
from backend.app.presentation.routes.health_routes import router as health_router
from backend.app.presentation.routes.document_routes import router as document_router
from backend.app.presentation.routes.image_routes import router as image_router

__all__ = ["health_router", "document_router", "image_router"]
