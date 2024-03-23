#!/usr/bin/python3
"""Test Amenity class"""
from tests.test_models.test_base_model import test_basemodel
from sqlalchemy import inspect
from sqlalchemy.sql import sqltypes
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test Amenity"""

    def __init__(self, *args, **kwargs):
        """Initialization"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity
        self.inspector = inspect(Amenity)

    def test_name2(self):
        """Test name"""
        new = self.value()
        i = self.inspector.columns['name']
        self.assertEqual(type(i.type), sqltypes.String)


if __name__ == "__main__":
    unittest.main()
