<<<<<<< HEAD
#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if models.storage_t == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade='all, delete', backref="state")
    else:
        name = ""

    if models.storage_t != "db":
        @property
        def cities(self):
            """returns the list of City instances with state_id = State.id"""
            from models import storage
            the_cities = storage.all(City)
            state_cities = []
            for city in the_cities.values():
                if city.state_id == self.id:
                    state_cities.append(city)
            return state_cities
