import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.api.api_v1.router import api_router
from app.core.logging_config import logger
from app.db.init_db import init_db

@asynccontextmanager
async def lifespan(app):
    """
    Lifespan context manager for the application.
    Handles startup and shutdown events.
    """
    # Startup logic
    logger.info("Starting up the S.I.E.N.A API...")
    init_db()
    yield
    # Shutdown logic
    logger.info("Shutting down the S.I.E.N.A API...")

# Create the FastAPI application (only once)
app = FastAPI(
    title="[CORE] S.I.E.N.A",
    description="Sistema Interno de Estratégia e Neutralização de Ameaças",
    version="0.1.0",
    lifespan=lifespan,
)

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router after app is defined
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    """
    Root endpoint.
    Returns a welcome message.
    """
    return {"message": "Welcome to the S.I.E.N.A API!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)