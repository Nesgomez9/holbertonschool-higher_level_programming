#!/usr/bin/python3
""" First model class """

from sqlalchemy import ForeignKey, Column, Integer, String
from model_state import Base


class City(Base):
    """ Class State """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
