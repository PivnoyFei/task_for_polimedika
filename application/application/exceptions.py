from fastapi import status
from fastapi.responses import JSONResponse
from starlette.requests import Request


async def message(request: Request, exc: Exception):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    message = ""
    for pydantic_error in exc.errors():
        loc, msg = pydantic_error["loc"], pydantic_error["msg"]
        filtered_loc = loc[1:] if loc[0] in ("body", "query", "path") else loc
        field_string = ".".join(filtered_loc)
        message += f"\n{field_string} - {msg}"
    return JSONResponse(
        {"detail": base_error_message, "errors": message},
        status.HTTP_400_BAD_REQUEST,
    )
