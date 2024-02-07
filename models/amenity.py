#!/usr/bin/python3
"""Class heritates from BaseModel:Parent"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Class heritate from the class BaseModel"""

    Identity = ""

    def __init__(self, *args, **kwargs):
        """initialization of Amenity"""
        super().__init__(self, *args, **kwargs)
