#!/usr/bin/python3
"""Unittests for StateClass """


import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Unit tests for the State class."""

    def setUp(self):
        """Set up test environment."""
        self.state = State()

    def test_inheritance(self):
        """Test that State inherits from BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributes(self):
        """Test the default attributes of State."""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, "")


if __name__ == "__main__":
    unittest.main()
