#!/usr/bin/python3
"""Defines the Place class."""


from models.base_model import BaseModel


class Place(BaseModel):
    """Place class that inherits from BaseModel.

    Attributes:
        city_id (str): The id of the city.
        user_id (str): The id of the user.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests.
        price_by_night (int): The price per night.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of amenity ids.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a Place instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
