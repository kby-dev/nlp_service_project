import uuid
from fastapi import Request

CORRELATION_HEADER = "X-Correlation-ID"

async def add_correlation_id(request: Request, call_next):
    """
    Middleware to generate a unique request ID for each request
    and attach it to the request state and response headers.
    """
    correlation_id = request.headers.get(CORRELATION_HEADER)
    if not correlation_id:
        correlation_id = str(uuid.uuid4())

    # Attach to request.state so downstream code can access it
    request.state.correlation_id = correlation_id

    # Process request
    response = await call_next(request)

    # Add header to response
    response.headers[CORRELATION_HEADER] = correlation_id

    return response
