from uuid import UUID, uuid4
from datetime import datetime
from beanie import Document
from pydantic import Field


class Skill(Document):
    id: UUID = Field(default_factory=uuid4)
    name: str
    category: str
    description: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
