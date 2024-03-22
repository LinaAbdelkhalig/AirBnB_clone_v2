#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, ForeignKey, String, Integer, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey('places.id'),
                             primary_key=True),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True))


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
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    # it said this is for DBStorage idk what that means ???
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False, backref="place_amenities")
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """Returns the list of reviews"""
            from models import storage
            review_objs = storage.all(Review)
            return [r for r in review_objs.values() if r.place_id == self.id]

        @property
        def amenities(self):
            """Returns the list of amenity instances"""
            from models import storage
            a_objects = storage.all(Amenity)
            return [a for a in a_objects if hasattr(a, 'id') and
                    a.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, value):
            """appends an Amenity.id to amenity_ids"""
            if isinstance(value, Amenity) and value.id not in self.amenity_ids:
                self.amenity_ids.append(value.id)
