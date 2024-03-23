#!/usr/bin/python3
"""Test Review class"""
from tests.test_models.test_base_model import test_basemodel
from sqlalchemy import inspect
from sqlalchemy.sql import sqltypes
from models.review import Review


class test_review(test_basemodel):
    """Test Review"""

    def __init__(self, *args, **kwargs):
        """Initialize"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review
        self.inspector = inspect(Review)

    def test_place_id(self):
        """Test place id"""
        new = self.value()
        i = self.inspector.columns['place_id']
        self.assertEqual(type(i.type), sqltypes.String)

    def test_user_id(self):
        """Test user_id"""
        new = self.value()
        i = self.inspector.columns['user_id']
        self.assertEqual(type(i.type), sqltypes.String)

    def test_text(self):
        """Test text"""
        new = self.value()
        i = self.inspector.columns['text']
        self.assertEqual(type(i.type), sqltypes.String)


if __name__ = "__main__":
    unittest.main()
