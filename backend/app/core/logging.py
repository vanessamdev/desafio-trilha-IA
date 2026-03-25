"""
Logging Configuration
"""
import logging
import sys
from datetime import datetime


class StructuredFormatter(logging.Formatter):
    """Structured log formatter"""
    
    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
        }
        
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        
        if hasattr(record, "request_id"):
            log_data["request_id"] = record.request_id
            
        return str(log_data)


def setup_logging(debug: bool = False) -> logging.Logger:
    """Configure application logging"""
    logger = logging.getLogger("app")
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(StructuredFormatter())
    
    logger.handlers.clear()
    logger.addHandler(handler)
    
    return logger


def get_logger() -> logging.Logger:
    """Get application logger"""
    return logging.getLogger("app")
