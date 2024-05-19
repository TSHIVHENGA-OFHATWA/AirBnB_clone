#!/usr/bin/python3
""" Unittests for Review Class"""


import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Unit tests for the Review class."""

    def setUp(self):
        """Set up test environment."""
        self.review = Review()

    def test_inheritance(self):
        """Test that Review inherits from BaseModel."""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        """Test the default attributes of Review."""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")


if __name__ == "__main__":
    unittest.main()
