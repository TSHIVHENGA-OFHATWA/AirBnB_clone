#!/usr/bin/python3
""" Unittests for User class """


import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Unit tests for the User class."""

    def setUp(self):
        """Set up test environment."""
        self.user = User()

    def test_inheritance(self):
        """Test that User inherits from BaseModel."""
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """Test the default attributes of User."""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))


if __name__ == "__main__":
    unittest.main()
