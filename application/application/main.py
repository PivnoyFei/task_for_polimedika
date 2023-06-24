from typing import Any

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic.error_wrappers import ValidationError
from starlette.exceptions import HTTPException
from starlette.requests import Request

from application.config import BACKEND_CORS_ORIGINS
from application.database import Base, engine
from application.exceptions import message
from application.router import router

app = FastAPI(
    title="Test task for polimedika",
    description=None,
    # root_path="/api/v1",
    # docs_url=None,
    openapi_url="/docs/openapi.json",
    redoc_url="/docs",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.on_event("startup")
# async def on_startup():
#     async with engine.begin() as conn:
#         # await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)


# @app.exception_handler(HTTPException)
# async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
#     return JSONResponse({"detail": f"{exc.detail}"}, exc.status_code)


# @app.exception_handler(ValidationError)
# async def validation_exception_pydantic(request: Request, exc: ValidationError) -> JSONResponse:
#     return await message(request, exc)


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(
#     request: Request, exc: RequestValidationError
# ) -> JSONResponse:
#     return await message(request, exc)


app.include_router(router, prefix="/api/v1")
