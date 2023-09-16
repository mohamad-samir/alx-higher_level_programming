#!/usr/bin/python3
"""
This module defines a City class that represents a table `cities`
in an SQL database.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from relationship_state import Base


class City(Base):
    """
    Represents a city in a database table.

    Attributes:
        id (int): The primary key for the table.
        name (str): The name of the city.
        state_id (int): The id of the state in the state table.
    """

    __tablename__ = 'cities'

    id: int = Column(Integer, primary_key=True)
    name: int = Column(String(128), nullable=False)
    state_id: int = Column(Integer, ForeignKey('states.id'))

    # state = relationship('State', back_populates='cities')
