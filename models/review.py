#!/usr/bin/python3
"""Class Heritate from Class BaseModel:parent"""

from models.base_model import BaseModel

class Review(BaseModel):
    """class heritating from BaseModel
      Args:
          place_id: input value
          user_id: input value
          text: input value
    """

    place_id = ""
    user_id = ""
    text= ""

    def __init__(self, *args, **kwargs):
        """initialization of Review"""
        super().__init__(self, *args, **kwargs)
