from fastapi import FastAPI, Request
from api.v1.classify import router as classify_router
from utils.logging_config import setup_logger
import json
from middleware.correlation_id import add_correlation_id

logger = setup_logger()

app = FastAPI(
    title="Service Category Classifier",
    version="1.0.0",
    description="Classifies user requests into service categories + license requirements"
)

app.middleware("http")(add_correlation_id)

# Middleware for logging
@app.middleware("http")
async def log_requests(request: Request, call_next):
    body = None
    if request.method == "POST":
        body = await request.body()
        try:
            body = json.loads(body.decode("utf-8"))
        except Exception:
            body = str(body)

    correlation_id = getattr(request.state, "correlation_id", "unknown")
    
    logger.info({
        "event": "request_received",
        "method": request.method,
        "url": str(request.url),
        "payload": body,
        "correlation_id": correlation_id
    })

    response = await call_next(request)

    logger.info({
        "event": "response_sent",
        "status_code": response.status_code,
        "url": str(request.url),
        "correlation_id": correlation_id
    })

    return response

# Register router
app.include_router(classify_router, prefix="/v1")