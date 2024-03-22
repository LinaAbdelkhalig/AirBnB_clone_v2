#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """
    The amenity class

    Attributes:
        __tablename__ (str): the name of the table in the db
        name (sqlalchemy.Column): the name of the amenity
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    # place_amenities = relationship("Place", secondary=place_amenity,
    #                                 viewonly=False)
