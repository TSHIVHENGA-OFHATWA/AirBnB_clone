#!/usr/bin/python3
"""Defines the Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel.

    Attributes:
        place_id (str): The id of the place.
        user_id (str): The id of the user.
        text (str): The review text.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a Review instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
