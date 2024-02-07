#!/usr/bin/python3
"""Class Heritate from Class BaseModel:parent"""

from models.base_model import BaseModel

class Place(BaseModel):
    """class heritating from BaseModel
      Args:
          city_id: input value
          user_id: input value
          name: input value
          description: input value
          number_rooms: input value
          number_bathrooms: input value
          max_guest: input value
          price_by_night: input value
          latitude: input valuelongitude: input value
          amenity_ids: input value
    """
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    name = ""

    def __init__(self, *args, **kwargs):
        """initialization of place"""
        super().__init__(self, *args, **kwargs)
