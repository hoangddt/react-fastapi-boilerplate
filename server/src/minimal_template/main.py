from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

from minimal_template.core.config import settings
from minimal_template.core.logging import setup_logging
from minimal_template.api.heroes.routes import router as heroes_router
from minimal_template.api.static_files.routes import router as static_files_router
from minimal_template.extensions import setup_rapidoc

# Set up logging configuration
setup_logging()

app = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG,
)


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(static_files_router)
app.include_router(heroes_router)

setup_rapidoc(app)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to Timeline API!"}
