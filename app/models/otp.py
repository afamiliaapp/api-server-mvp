from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime

from app.database.base import Base


class OTP(Base):

    __tablename__ = "otp_codes"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, index=True)

    code = Column(String)

    expires_at = Column(DateTime)

    is_used = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)