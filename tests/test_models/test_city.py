#!/usr/bin/python3
"""Test City class"""
from tests.test_models.test_base_model import test_basemodel
from sqlalchemy import inspect
from sqlalchemy.sql import sqltypes
from models.city import City


class test_City(test_basemodel):
<<<<<<< HEAD
    """Test City"""

    def __init__(self, *args, **kwargs):
        """Initialize"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City
        self.inspector = inspect(City)

    def test_state_id(self):
        """Test state_id"""
        new = self.value()
        i = self.inspector.columns['state_id']
        self.assertEqual(type(i.type), sqltypes.String)

    def test_name(self):
        """Test name"""
        new = self.value()
        i = self.inspector.columns['name']
        self.assertEqual(type(i.type), sqltypes.String)


if __name__ == "__main__":
    unittest.main()
