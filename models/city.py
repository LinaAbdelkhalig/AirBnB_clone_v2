#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel):
    """
    The city class

    Attributes:
        __tablename__ (str): the name of the table in the db
        name (sqlalchemy.Column) : the name of the state
        state_id (sqlalchemy.Column): the id of the state
    """

    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey('states.id'))
    places = relationship("Place", backref="cities", cascade="all, delete")
