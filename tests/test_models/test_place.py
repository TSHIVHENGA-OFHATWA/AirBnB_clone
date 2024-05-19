#!/usr/bin/python3
""" Unittest for Place class"""


import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Unit tests for the Place class."""

    def setUp(self):
        """Set up test environment."""
        self.place = Place()

    def test_inheritance(self):
        """Test that Place inherits from BaseModel."""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attributes(self):
        """Test the default attributes of Place."""
        attributes = ['city_id', 'user_id', 'name', 'description',
                      'number_rooms', 'number_bathrooms', 'max_guest',
                      'price_by_night', 'latitude', 'longitude', 'amenity_ids']
        for attr in attributes:
            self.assertTrue(hasattr(self.place, attr))


if __name__ == "__main__":
    unittest.main()
