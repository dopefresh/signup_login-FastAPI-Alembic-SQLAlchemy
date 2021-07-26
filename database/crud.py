from sqlalchemy import select, update, func
from sqlalchemy.orm import lazyload, joinedload

from .connection import engine, pool, Base
from .models import User


def get_user(username: str):
    with pool() as session:
        with session.begin():
            query = select(User).where(username == username)
            result = session.execute(query)
            return result.scalar()
