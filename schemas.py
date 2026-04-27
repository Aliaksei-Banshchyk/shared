from datetime import datetime
from typing import Optional
from pydantic import BaseModel, field_validator
import re


# ── User ──────────────────────────────────────────────────────────────────────

class UserCreate(BaseModel):
    login: str
    password: str
    name: str

    @field_validator("login")
    @classmethod
    def login_must_be_valid(cls, v: str) -> str:
        if len(v) < 3:
            raise ValueError("login must be at least 3 characters")
        if not re.match(r"^[a-zA-Z0-9_]+$", v):
            raise ValueError("login may only contain letters, digits, and underscores")
        return v

    @field_validator("password")
    @classmethod
    def password_strength(cls, v: str) -> str:
        if len(v) < 6:
            raise ValueError("password must be at least 6 characters")
        return v


class UserUpdate(BaseModel):
    name: Optional[str] = None
    password: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    login: str
    name: str
    model_config = {"from_attributes": True}


class LoginRequest(BaseModel):
    login: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ── Event ─────────────────────────────────────────────────────────────────────

class EventCreate(BaseModel):
    event_date: datetime
    place: str
    description: Optional[str] = None


class EventUpdate(BaseModel):
    event_date: Optional[datetime] = None
    place: Optional[str] = None
    description: Optional[str] = None


class EventResponse(BaseModel):
    id: int
    event_date: datetime
    place: str
    description: Optional[str]
    model_config = {"from_attributes": True}


# ── Booking ───────────────────────────────────────────────────────────────────

class BookingCreate(BaseModel):
    event_id: int


class BookingUpdate(BaseModel):
    event_id: Optional[int] = None


class BookingResponse(BaseModel):
    id: int
    user_id: int
    event_id: int
    booking_date: datetime
    model_config = {"from_attributes": True}


class ScheduleItem(BaseModel):
    booking_id: int
    event_id: int
    event_date: datetime
    place: str
    description: Optional[str]
    booking_date: datetime
    model_config = {"from_attributes": True}


# ── Feedback ──────────────────────────────────────────────────────────────────

class FeedbackCreate(BaseModel):
    event_id: int
    message: str


class FeedbackUpdate(BaseModel):
    message: Optional[str] = None


class FeedbackResponse(BaseModel):
    id: int
    event_id: int
    user_id: int
    message: str
    created_at: datetime
    model_config = {"from_attributes": True}


# ── Broker ────────────────────────────────────────────────────────────────────

class BrokerMessage(BaseModel):
    issue_date_time_utc: datetime
    user_id: int
    booking_id: int
    message: str
