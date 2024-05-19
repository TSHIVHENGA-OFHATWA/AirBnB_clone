#!/usr/bin/python3
"""Defines the Amenity class."""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel.

    Attributes:
        name (str): The name of the amenity.
    """

    def __init__(self, *args, **kwargs):
        """Initializes an Amenity instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
