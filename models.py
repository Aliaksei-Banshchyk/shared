from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, event, text
from sqlalchemy.orm import relationship
from database import Base

SCHEMA = "Aliaksei_Banshchyk"


@event.listens_for(Base.metadata, "before_create")
def create_schema(target, connection, **kw):
    if connection.dialect.name == "mssql":
        connection.execute(text(
            f"IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = '{SCHEMA}') "
            f"EXEC('CREATE SCHEMA [{SCHEMA}]')"
        ))

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    name = Column(String(150), nullable=False)

    bookings = relationship("Booking", back_populates="user")


class Event(Base):
    __tablename__ = "events"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True, index=True)
    event_date = Column(DateTime, nullable=False)
    place = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

    bookings = relationship("Booking", back_populates="event")
    feedbacks = relationship("Feedback", back_populates="event")


class Booking(Base):
    __tablename__ = "bookings"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(f"{SCHEMA}.users.id"), nullable=False)
    event_id = Column(Integer, ForeignKey(f"{SCHEMA}.events.id"), nullable=False)
    booking_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="bookings")
    event = relationship("Event", back_populates="bookings")


class Feedback(Base):
    __tablename__ = "feedbacks"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey(f"{SCHEMA}.events.id"), nullable=False)
    user_id = Column(Integer, ForeignKey(f"{SCHEMA}.users.id"), nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    event = relationship("Event", back_populates="feedbacks")
    user = relationship("User")
