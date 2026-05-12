import os
import httpx
from typing import Optional

USER_SERVICE_URL     = os.getenv("USER_SERVICE_URL",     "http://user-service:8001")
EVENT_SERVICE_URL    = os.getenv("EVENT_SERVICE_URL",    "http://event-service:8002")
BOOKING_SERVICE_URL  = os.getenv("BOOKING_SERVICE_URL",  "http://booking-service:8003")
FEEDBACK_SERVICE_URL = os.getenv("FEEDBACK_SERVICE_URL", "http://feedback-service:8004")

TIMEOUT = 10.0

def get(url: str, token: Optional[str] = None) -> httpx.Response:
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    return httpx.get(url, headers=headers, timeout=TIMEOUT)

def post(url: str, payload: dict, token: Optional[str] = None) -> httpx.Response:
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    return httpx.post(url, json=payload, headers=headers, timeout=TIMEOUT)

def patch(url: str, payload: dict, token: Optional[str] = None) -> httpx.Response:
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    return httpx.patch(url, json=payload, headers=headers, timeout=TIMEOUT)

def delete(url: str, token: Optional[str] = None) -> httpx.Response:
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    return httpx.delete(url, headers=headers, timeout=TIMEOUT)