#!/usr/bin/python3
"""
Script that creates an ORM table with SQLAlchemy
creating an model class
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class State(Base):
    """Base model state class"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
