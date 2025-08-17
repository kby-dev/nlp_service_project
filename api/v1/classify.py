from fastapi import APIRouter, HTTPException, Request
from models.request_model import ServiceRequest, ServiceResponse
from services.nlp import classify_service
from services.license_engine import get_license_requirement
from utils.logging_config import setup_logger

router = APIRouter()
logger = setup_logger()

@router.post("/", response_model=ServiceResponse)
async def classify_request_endpoint(request: ServiceRequest, fastapi_request: Request):
    """
    Classify a service request into category + license requirement
    and log both request payload and result.
    """
    correlation_id = getattr(fastapi_request.state, "correlation_id", "unknown")
    try:
        # NLP Classification
        category = classify_service(request.problem)
        
        # License determination
        license_type = get_license_requirement(category)
        
        # Log classification result
        logger.info({
            "event": "classification_result",
            "input": request.problem,
            "category": category,
            "license_type": license_type
        })
        
        return ServiceResponse(
            category=category,
            license_type=license_type
        )

    except Exception as e:
        logger.error({
            "event": "classification_error",
            "error": str(e),
            "input": request.dict()
        })
        raise HTTPException(status_code=500, detail="Internal Server Error")
