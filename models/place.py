#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column,ForeignKey, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City #not sure about this one pls check


class Place(BaseModel, Base):
    """ 
    A place to stay

    Attributes:
        __tablename__: the name of the mysql table
        city_id (sqlalchemy.Column): the id of the city where the place is
        user_id (sqlalchemy.Column): the user staying in the place
        name (sqlalchemmy.Column): the name of the place?
        description (sqlalchemy.Column): the desctiption of the place
        number_rooms (sqlalchemy.Column): the number of rooms in place
        number_bathrooms (sqlalchemy.Column): the number of bathrooms
        max_guest (sqlalchemy.Column): the max number of guests allowed
        price_by_night (sqlalchemy.Column): the price of the night
        latitude (sqlalchemy.Column): the latitude
        longitude (sqlalchemy.Column): the longitude
        amneity_ids (list): ??
    """
    __tablename__ = 'places'
    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    # it said this is for DBStorage idk what that means ???
    reviews = relationship("Review" backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)
    amenity_ids = []

    # getter attribute here
    @property
    def amenities(self):
        """Returns the list of amenity instances"""
        return self.amenity_ids

    @amenities.setter
    def amenities(self, value):
        """appends an Amenity.id to amenity_ids"""
        if isinstance(value, Amenity):
            self.amenity_ids.append(value.id)
