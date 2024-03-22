#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """
    This class defines a user

    Atributes:
        __tablename__ (str): the name of the table
        email (sqlalchemy.Column): the email of the user
        password (sqlalchemy.Column): the user password
        first_name (sqlalchemy.Column): the first name of the user
        last_name (sqlalchemy.Column): the last name of the user
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="all, delete")
    reviews = relationship("Review", backref="user", cascade="all, delete")
