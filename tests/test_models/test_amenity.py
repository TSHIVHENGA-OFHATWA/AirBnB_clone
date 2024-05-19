#!/usr/bin/python3
"""Unittests for amenity class """


import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Unit tests for the Amenity class."""

    def setUp(self):
        """Set up test environment."""
        self.amenity = Amenity()

    def test_inheritance(self):
        """Test that Amenity inherits from BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """Test the default attributes of Amenity."""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "")


if __name__ == "__main__":
    unittest.main()
