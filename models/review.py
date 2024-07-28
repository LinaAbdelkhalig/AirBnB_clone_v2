#!/usr/bin/python3
""" Review module for the HBNB project """

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """
    Review classto store review information

    Attributes:
        __tablename__ (str): the name of the mysql table
        text (sqlalchemy.Column): the review text body
        place_id (sqlalchemy.Column): the id of the place to be reviewed
        user_id (sqlalchemy.Column): the id of the user posting the review
    """
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
