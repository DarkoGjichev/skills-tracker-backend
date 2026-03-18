from contextlib import asynccontextmanager
from pymongo import AsyncMongoClient
from fastapi import FastAPI
from beanie import init_beanie
from models.skill import Skill
from models.user import User


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        client = AsyncMongoClient("mongodb://admin:password@localhost:27019/")
        await init_beanie(
            database=client["skills_tracker_db"], document_models=[Skill, User]
        )
    except Exception:
        raise

    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}
