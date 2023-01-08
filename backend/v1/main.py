import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.app.app import router
from server.routes.country import router as country_router

#########
# logger
#
log = logging.getLogger("uvicorn.error")

description = """
## SITE ANNONCE
Idee de AVITO
"""

app = FastAPI(
    docs_url="/api/doc",
    redoc_url="/api/redoc",
    title="Site Annonces",
    description=description,
    contact={
        "name": "VIH",
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=False,
)
app.include_router(country_router, tags=["Country"])
app.include_router(router, prefix="/api")
