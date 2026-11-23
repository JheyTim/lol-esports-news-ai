from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import initialize_database
from app.routers.articles import router as articles_router

# =====================================
# 1. APPLICATION STARTUP
# =====================================


@asynccontextmanager
async def lifespan(app: FastAPI):

    initialize_database()

    yield


# =====================================
# 2. CREATE FASTAPI APPLICATION
# =====================================

app = FastAPI(
    title="League of Legends Esports News API",
    description="Backend API for our LoL esports news platform.",
    version="0.1.0",
    lifespan=lifespan,
)


# =====================================
# 3. REGISTER ARTICLE ROUTER
# =====================================

app.include_router(articles_router)


# =====================================
# 4. ROOT ENDPOINT
# =====================================


@app.get("/")
def read_root():

    return {"message": "League of Legends Esports News API is running!", "status": "ok"}


# =====================================
# 5. HEALTH CHECK
# =====================================


@app.get("/health")
def health_check():

    return {"status": "healthy"}
