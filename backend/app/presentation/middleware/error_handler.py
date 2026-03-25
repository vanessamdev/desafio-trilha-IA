"""
Error Handler Middleware
"""
import uuid
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from backend.app.core.exceptions import AppException
from backend.app.core.logging import get_logger


class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    """Global error handler middleware"""
    
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())[:8]
        logger = get_logger()
        
        try:
            response = await call_next(request)
            return response
            
        except AppException as exc:
            logger.error(
                f"[{request_id}] {exc.error_code}: {exc.message}",
                extra={"request_id": request_id}
            )
            return JSONResponse(
                status_code=exc.status_code,
                content={
                    "error": exc.error_code,
                    "message": exc.message,
                    "request_id": request_id
                }
            )
            
        except Exception as exc:
            logger.exception(
                f"[{request_id}] Unexpected error: {str(exc)}",
                extra={"request_id": request_id}
            )
            return JSONResponse(
                status_code=500,
                content={
                    "error": "INTERNAL_ERROR",
                    "message": "An unexpected error occurred",
                    "request_id": request_id
                }
            )
