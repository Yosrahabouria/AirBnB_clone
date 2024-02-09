#!/usr/bin/python3
"""Class Heritate from Class BaseModel:parent"""

from models.base_model import BaseModel


class User(BaseModel):
    """class heritating from BaseModel
      Args:
          email: input value
          password: input value
          first_name: input value
          last_name: input value
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initialization of User"""
        super().__init__(self, *args, **kwargs)
