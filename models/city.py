#!/usr/bin/python3
"""Class Heritate from Class BaseModel:parent"""

from models.base_model import BaseModel

class City(BaseModel):
    """class heritating from BaseModel
      Args:
          state_id: input value
          name: input value
    """

    state_id = ""
    name = ""
    
    def __init__(self, *args, **kwargs):
        """initialization of City"""
        super().__init__(self, *args, **kwargs)
