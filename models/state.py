#!/usr/bin/python3
"""Defines the State class."""

from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel.

    Attributes:
        name (str): The name of the state.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a State instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
