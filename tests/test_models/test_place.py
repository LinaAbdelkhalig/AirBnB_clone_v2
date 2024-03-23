#!/usr/bin/python3
"""Test Place class"""
from tests.test_models.test_base_model import test_basemodel
from sqlalchemy import inspect
from sqlalchemy.sql import sqltypes
from models.place import Place


class test_Place(test_basemodel):
    """Test Place"""

    def __init__(self, *args, **kwargs):
        """Initialize"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place
        self.inspector = inspect(Place)

    def test_city_id(self):
        """Test city_id"""
        new = self.value()
        i = self.inspector.columns['city_id']
        self.assertEqual(type(i.type), sqltypes.String)

    def test_user_id(self):
        """Test user_id"""
        new = self.value()
        i = self.inspector.columns['user_id']
        self.assertEqual(type(i.type), sqltypes.String)

    def test_name(self):
        """Test name"""
        new = self.value()
        i = self.inspector.columns['name']
        self.assertEqual(type(i.type), sqltypes.String)

    def test_description(self):
        """Test description"""
        new = self.value()
        i = self.inspector.columns['description']
        self.assertEqual(type(i.type), sqltypes.String)

    def test_number_rooms(self):
        """Test number_rooms"""
        new = self.value()
        i = self.inspector.columns['number_rooms']
        self.assertEqual(type(i.type), sqltypes.Integer)

    def test_number_bathrooms(self):
        """Test number_bathrooms"""
        new = self.value()
        i = self.inspector.columns['number_bathrooms']
        self.assertEqual(type(i.type), sqltypes.Integer)

    def test_max_guest(self):
        """Test max_guest"""
        new = self.value()
        i = self.inspector.columns['max_guest']
        self.assertEqual(type(i.type), sqltype.Integer)

    def test_price_by_night(self):
        """Test price_by_night"""
        new = self.value()
        i = self.inspector.columns['price_by_night']
        self.assertEqual(type(i.type), sqltypes.Integer)

    def test_latitude(self):
        """Test latitude"""
        new = self.value()
        i = self.inspector.columns['latitude']
        self.assertEqual(type(i.type), sqltypes.Float)

    def test_longitude(self):
        """Test longitude"""
        new = self.value()
        i = self.inspector.columns['longitude']
        self.assertEqual(type(i.type), sqltypes.Float)

    def test_amenity_ids(self):
        """Test amenity_ids"""
        new = self.value()
        i = self.inspector.columns['amenity_ids']
        self.assertEqual(type(i.type), sqltypes.List)


if __name__ == "__main__":
    unittest.main()
