from pydantic import BaseModel
from typing import List, Optional

class ServiceRequest(BaseModel):
    name: str
    location: str
    problem: str
    image_urls: Optional[List[str]] = []

class ServiceResponse(BaseModel):
    category: str 
    license_type: str
