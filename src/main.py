import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from config import settings
from logger import log_requests
from todo.router import router as todo_router


app = FastAPI()

# Enable CORS with secure configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors.allowed_origins_list,  # Defaults to localhost:5173, configurable via env
    allow_credentials=settings.cors.allow_credentials_bool,
    allow_methods=settings.cors.allowed_methods_list,
    allow_headers=settings.cors.allowed_headers_list,
)


# Add request logging middleware
app.middleware("http")(log_requests)


# Include route modules
app.include_router(todo_router, prefix="/api/todo", tags=["todo"])


# Mount static files (frontend) - only if static directory exists
if os.path.exists("static"):
    app.mount("/", StaticFiles(directory="static", html=True), name="static")