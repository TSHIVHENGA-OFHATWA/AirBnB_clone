#!/usr/bin/python3
"""Unit tests for City Class """


import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Unit tests for the City class."""

    def setUp(self):
        """Set up test environment."""
        self.city = City()

    def test_inheritance(self):
        """Test that City inherits from BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """Test the default attributes of City."""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")


if __name__ == "__main__":
    unittest.main()
