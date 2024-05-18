#!/usr/bin/python3


'''This module defines class BaseMmodel and be parent class for other classes.

Classes:
    BaseModel

Example:
    instance = BaseModel()
    print(instance)
    # [BaseModel] (<id>) {'id': <id>, 'created_at':
        <datetime>, 'updated_at': <datetime>}
    instance.save()
    print(instance.to_dict())
    # {'id': <id>, 'created_at': <iso_datetime>, 'updated_at':
        <iso_datetime>, '__class__': 'BaseModel'}
'''


import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes.

    Attributes:
        id (str): Unique identifer for each instance, generated using uuid4.
        created_at (datetime): The datetime for instance was created.
        updated_at (datetime): The datetime for the instance was last updated.
    """

    def __init__(self):
        """Initializes a new instance of BaseModel.

        Sets the id, created_at, and uodated_at attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance.

        Returns:
            str: A string in the format
                [<class name>] (self.id) <self.__dict__>.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing representation of the instance.

        Converts the created_at and updated_at to ISO format strings.

        Returns:
            dict: A dictionary conataining all keys/value of__dict__
                    of the instance, with an additional
                    key __class__ set to the class name.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
