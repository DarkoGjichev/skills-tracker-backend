from uuid import UUID, uuid4
from datetime import datetime
from beanie import Document, Link
from pydantic import Field
from models.skill import Skill


class User(Document):
    id: UUID = Field(default_factory=uuid4)
    name: str
    title: str
    email: str
    skills: list[Link[Skill]] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
