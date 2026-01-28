from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True)
    jd_url = Column(String)
    extracted_text = Column(Text)
    generated_resume = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
