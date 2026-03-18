from uuid import UUID
from pydantic import BaseModel
from datetime import datetime


class SkillCreate(BaseModel):
    name: str
    category: str
    description: str


class SkillUpdate(BaseModel):
    name: str | None = None
    category: str | None = None
    description: str | None = None


class SkillResponse(BaseModel):
    id: UUID
    name: str
    category: str
    description: str
    created_at: datetime
    updated_at: datetime
