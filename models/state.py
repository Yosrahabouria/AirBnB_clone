#!/usr/bin/python3
"""Class Heritate from Class BaseModel:parent"""

from models.base_model import BaseModel

class State(BaseModel):
    """class heritating from BaseModel
      Args:
          name: input value
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """initialization of State"""
        super().__init__(self, *args, **kwargs)
