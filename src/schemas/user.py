from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime
from schemas.skill import SkillResponse


class UserCreate(BaseModel):
    name: str
    title: str
    email: str
    skills: list[UUID] = Field(default_factory=list)


class UserUpdate(BaseModel):
    name: str | None = None
    title: str | None = None
    email: str | None = None
    skills: list[UUID] = Field(default_factory=list)


class UserResponse(BaseModel):
    id: UUID
    name: str
    title: str
    email: str
    skills: list[SkillResponse]
    created_at: datetime
    updated_at: datetime
