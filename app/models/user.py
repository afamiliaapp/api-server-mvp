from sqlalchemy import Column, Integer, String
from app.database.base import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, index=True)

    firstname = Column(String)

    surname = Column(String)

    password_hash = Column(String)