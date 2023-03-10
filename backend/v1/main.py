import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.app.app import router
from server.routes.articles import router as article_router
from server.routes.category import router as category_router
from server.routes.userProfile import router as userProfile_router

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
app.include_router(article_router, tags=["Article"])
app.include_router(category_router, tags=["Category"])
app.include_router(userProfile_router, tags=["User"])
app.include_router(router, prefix="/api")
