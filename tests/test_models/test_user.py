#!/usr/bin/python3
"""Tests the User class"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from sqlalchemy import inspect
from sqlalchemy.sql import sqltypes


class test_User(test_basemodel):
    """Test the User class"""

    def __init__(self, *args, **kwargs):
        """Initialize"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User
        self.inspector = inspect(User)

    def test_first_name(self):
        """Test the first name"""
        new = self.value()
        i = self.inspector.columns['first_name']
        self.assertEqual(type(i.type), sqltypes.String)

    def test_last_name(self):
        """Test the last name"""
        new = self.value()
        i = self.inspector.colums['last_name']
        self.assertEqual(type(i.type), sqltypes.String)

    def test_email(self):
        """Test the email"""
        new = self.value()
        i = self.inspector.columns['email']
        self.assertEqual(type(i.type), sqltypes.String)

    def test_password(self):
        """Test the password"""
        new = self.value()
        i = self.inspector.columns['password']
        self.assertEqual(type(i.type), sqltypes.String)


if __name__ == "__main__":
    unittest.main()
