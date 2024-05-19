#!/usr/bin/python5
"""FileStorage class for handling JSON (de)serialization of instances."""

import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    """Serializes and deserializes JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary storing all objects by <class name>.id.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects.

        Returns:
            dict: Dictionary of all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """Add a new object to __objects.

        Args:
            obj (BaseModel): The object to add.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        serialized_objs = {
                key: obj.to_dict() for key, obj in self.__objects.items()
                }
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """Deserialize the JSON file to __objects, if it exists."""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                try:
                    loaded_objs = json.load(file)
                    for key, value in loaded_objs.items():
                        self.__objects[key] = BaseModel(**value)
                except Exception as e:
                    print("Error loading objects from JSON:", e)
