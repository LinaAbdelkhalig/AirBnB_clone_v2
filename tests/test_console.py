#!/usr/bin/python3
"""This module tests the console.py"""

from console import HBNBCommand
from io import StringIO
import json
import models
from models import storage
import os
import sys
import unittest
from unittest.mock import patch


class test_console(unittest.TestCase):
    """Tests the console"""
    def setUp(self):
        """Setup"""
        self.commands = HBNBCommand().get_names()
        pass

    def tearDown(self):
        """Reset"""
        pass

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') = 'db', 'Not FileStorage')
    def test_empty_line(self):
        """Tests empty lines"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("                    \n")
            self.assertEqual(f.getvalue(), '')

    def test_quit(self):
        """Tests quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), '')

    def test_EOF(self):
        """Tests EOF"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), '\n')


class TestConsoleWithoutDot(unittest.TestCase):
    """Tests the classes commands without dot [all User]"""
    def setUp(self):
        """Setup"""
        self.classes = ['BaseModel', 'User', 'State', 'City'
                        'Amenity', 'Place', 'Review']
        pass

    def tearDown(self):
        """Reset"""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    # def test_create(self):
    #     """Tests [create <className>]"""
    #     for cls in self.classes:
    #         with patch('sys.stdout', new=StringIO()) as f:
    #                 HBNBCommand().onecmd(f"create {cls}")
    #                 print(f.getvalue())
    #                 self.assertIsInstance(f.getvalue().strip(), str)

    def test_all_with_class_name(self):
        """Tests [all <className>]"""
        # for cls in self.classes:
        #     with patch('sys.stdout', new=StringIO()) as f:
        #         for cls in self.classes:
        #             HBNBCommand().onecmd(f"all {cls}")
        #             for instance in json.loads(f.getvalue()):
        #                 self.assertEqual(instance.split()[0], f'[{cls}]')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all wrongClsName")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_show(self):
        """Tests [show <className> <id>]"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show WrongClassName")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User WrongInstance")
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            b = models.base_model.BaseModel()
            b.age = 10
            HBNBCommand().onecmd(f"show BaseModel {b.id}")
            out = f"[{type(b).__name__}] ({b.id}) {b.__dict__}"
            self.assertEqual(f.getvalue().strip(), out)

    def test_update(self):
        """Tests [update BaseModel 1234-1234-1234 email "aibnb@mail.com"]"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update WrongClassName")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User WrongInstance")
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            b = models.base_model.BaseModel()
            b.age = 10
            HBNBCommand().onecmd(f"update BaseModel {b.id}")
            self.assertEqual(f.getvalue(), "** attribute name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            b = models.base_model.BaseModel()
            b.age = 10
            HBNBCommand().onecmd(f"update BaseModel {b.id} age")
            self.assertEqual(f.getvalue(), "** value missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            b = models.base_model.BaseModel()
            b.age = 10
            HBNBCommand().onecmd(f"update BaseModel {b.id} age 5")
            self.assertEqual(b.age, 5)

    def test_destroy(self):
        """Tests destroy BaseModel 1234-1234-1234"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy WrongClassName")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User WrongInstance")
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            b = models.base_model.BaseModel()
            b.age = 10
            HBNBCommand().onecmd("destroy BaseModel {b.id}")


if __name__ == '__main__':
    unittest.main()
