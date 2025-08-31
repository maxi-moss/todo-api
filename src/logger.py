"""
Logging utilities for RAG comparison application.

Provides request/response middleware for FastAPI with structured JSON logging.
"""

import json
import logging
import time
from fastapi import Request

# Configure structured logging for the application.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)

# Create request logger.
request_logger = logging.getLogger("requests")


def log_structured(logger: logging.Logger, level: int, message: str, **kwargs):
    """Log structured data as JSON.
    
    Args:
        logger: Logger instance to use.
        level: Logging level (e.g., logging.INFO).
        message: Human-readable log message.
        **kwargs: Additional data to include in the log entry.
    """
    # Create structured log entry with timestamp and custom fields.
    log_data = {
        "message": message,
        "timestamp": time.time(),
        **kwargs
    }
    # Output as JSON string for structured logging systems.
    logger.log(level, json.dumps(log_data, default=str))


async def log_requests(request: Request, call_next):
    """FastAPI middleware to log HTTP requests with metrics.
    
    Logs request details, response status, timing, and errors.

    Args:
        request: The incoming FastAPI request.
        call_next: Next middleware or route handler.

    Returns:
        The HTTP response from downstream handlers.
    """
    # Record start time for response time calculation.
    start_time = time.time()
    
    # Extract comprehensive request information for logging.
    request_info = {
        "method": request.method,
        "path": request.url.path,
        "query_params": dict(request.query_params),
        "client_ip": request.client.host if request.client else None,
        "user_agent": request.headers.get("user-agent"),
    }
    
    # Log request initiation with full context.
    log_structured(
        request_logger,
        logging.INFO,
        "Request started",
        **request_info
    )
    
    try:
        # Process the request through the application.
        response = await call_next(request)
        
        # Calculate total processing time.
        process_time_ms = (time.time() - start_time) * 1000
        
        # Log successful request completion with metrics.
        log_structured(
            request_logger,
            logging.INFO,
            "Request completed",
            status_code=response.status_code,
            response_time_ms=process_time_ms,
            **request_info
        )
        
        return response
        
    except Exception as e:
        # Calculate processing time even for failed requests.
        process_time_ms = (time.time() - start_time) * 1000
        
        # Log request failure with error details and timing.
        log_structured(
            request_logger,
            logging.ERROR,
            "Request failed",
            error=str(e),
            error_type=type(e).__name__,
            response_time_ms=process_time_ms,
            **request_info
        )
        # Re-raise exception to maintain normal error handling flow.
        raise