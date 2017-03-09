import uuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Text, String, Integer, BIGINT, DateTime, Boolean, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB

from app import app

db = SQLAlchemy(app)
