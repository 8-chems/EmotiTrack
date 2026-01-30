import logging
import time

from fastapi import Request

logger = logging.getLogger("emotitrack.middleware")


async def log_requests_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    logger.info(
        "%s %s completed in %.3fs status=%s",
        request.method,
        request.url.path,
        duration,
        response.status_code,
    )
    return response
