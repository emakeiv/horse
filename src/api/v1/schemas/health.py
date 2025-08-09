from uuid import uuid4
from datetime import datetime, timezone
from pydantic import BaseModel, Field

from .common import Status

class HealthCheckResponse(BaseModel):
    """
    Response structure for /health endpoint call
    """
    instance: str = Field(default_factory=lambda : uuid4().hex)
    stamp:    datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    status:   str = Field(default=Status.OK)