#!/usr/bin/python3
"""Defines the City class."""


from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel.

    Attributes:
        state_id (str): The id of the state.
        name (str): The name of the city.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a City instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
