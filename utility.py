"""
Shared HTTP utility for inter-service calls.
Each service uses these helpers to talk to other services.
"""

import httpx
from typing import Optional

# ── Service base URLs (update to match your deployment) ──────────────────────
USER_SERVICE_URL    = "http://localhost:8001"
EVENT_SERVICE_URL   = "http://localhost:8002"
BOOKING_SERVICE_URL = "http://localhost:8003"
FEEDBACK_SERVICE_URL= "http://localhost:8004"

TIMEOUT = 10.0  # seconds


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
