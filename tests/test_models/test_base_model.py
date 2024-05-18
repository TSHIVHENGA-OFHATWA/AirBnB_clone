#!/usr/bin/python3
""" Tests for BaseModel """


import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class."""

    def setUp(self):
        """Set up test environment."""
        self.model = BaseModel()

    def test_id_is_unique(self):
        """Test that id is unique and a string."""
        other_model = BaseModel()
        self.assertNotEqual(self.model.id, other_model.id)
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object."""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object."""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_representation(self):
        """Test the string representation of the BaseModel instance."""
        expected_str = "[BaseModel] ({}) {}".format(
                self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_save_method(self):
        """Test the save method updates updated_at attribute."""
        old_updated_at = self.model.updated_at
        sleep(0.1)
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertGreater(new_updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method returns the correct dictionary."""
        obj_dict = self.model.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], self.model.id)
        self.assertEqual(
                obj_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(
                obj_dict['updated_at'], self.model.updated_at.isoformat())
        self.assertEqual(
                obj_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(
                obj_dict['updated_at'], self.model.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
