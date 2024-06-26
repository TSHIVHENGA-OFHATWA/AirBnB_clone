#!/usr/bin/python3
"""FileStorage class for handling JSON (de)serialization of instances."""

import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


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
                        class_name, obj_id = key.split('.')
                        cls = globals().get(class_name)
                        if cls:
                            self.__objects[key] = cls(**value)
                except Exception as e:
                    print("Error loading objects from JSON:", e)
