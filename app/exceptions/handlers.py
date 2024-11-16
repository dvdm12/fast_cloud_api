from fastapi.responses import JSONResponse
from fastapi import Request
from starlette.exceptions import HTTPException as StarletteHTTPException

async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

async def validation_exception_handler(request: Request, exc):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()}
    )
