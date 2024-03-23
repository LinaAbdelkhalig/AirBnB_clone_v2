#!/usr/bin/python3
"""Test State class"""
from tests.test_models.test_base_model import test_basemodel
from sqlalchemy import inspect
from sqlalchemy.sql import sqltypes
from models.state import State


class test_state(test_basemodel):
    """Test State class"""

    def __init__(self, *args, **kwargs):
        """Initialize"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State
        self.inspector = inspect(State)

    def test_name3(self):
        """Test name"""
        new = self.value()
        i = self.inspector.columns['name']
        self.assertEqual(type(i.type), sqltypes.String)


if __name__ == "__main__":
    unittest.main()
