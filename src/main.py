from contextlib import asynccontextmanager
from pymongo import AsyncMongoClient
from fastapi import FastAPI
from beanie import init_beanie


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        client = AsyncMongoClient("mongodb://admin:password@localhost:27019/")
        await init_beanie(database=client["skills_tracker_db"])
    except Exception:
        raise

    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}
