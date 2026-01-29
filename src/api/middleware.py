from fastapi import FastAPI, Request
import logging

logging.basicConfig(level=logging.INFO)

async def log_request(request: Request):
    logging.info(f"Request: {request.method} {request.url}")

app.middleware("http")(log_request)
