#!/usr/bin/python3


'''This module defines class BaseMmodel and be parent class for other classes.

Classes:
    BaseModel
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

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

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
        from models import storage
        storage.save()

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
