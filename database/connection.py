from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from keys import POSTGRES_URI

Base = declarative_base()

engine = create_engine(POSTGRES_URI)
pool = sessionmaker(bind=engine, expire_on_commit=False, autoflush=False)
