#!/usr/bin/python3
""" Unittest for the storage solution """


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json


class TestFileStorage(unittest.TestCase):
    """Unit tests for the FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.file_path = FileStorage._FileStorage__file_path
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_returns_dict(self):
        """Test that all returns the __objects dictionary."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_adds_object(self):
        """Test that new adds an object to __objects."""
        initial_len = len(self.storage.all())
        self.storage.new(self.model)
        self.assertEqual(len(self.storage.all()), initial_len + 1)
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.assertIn(key, self.storage.all())

    def test_save_creates_file(self):
        """Test that save creates a file and saves objects."""
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
            self.assertIn(key, data)
            self.assertEqual(data[key], self.model.to_dict())

    def test_reload_loads_objects(self):
        """Test that reload loads objects from file."""
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.assertIn(key, self.storage.all())
        self.assertIsInstance(self.storage.all()[key], BaseModel)


if __name__ == "__main__":
    unittest.main()
