from sqlalchemy import Table, Column, DateTime, ForeignKey, func, Integer, String, Boolean, Text, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from .connection import Base

import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
     
    __mapper_args__ = {"eager_defaults": True}



