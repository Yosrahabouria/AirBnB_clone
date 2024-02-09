#!/usr/bin/python3
"""
that defines all common attributes/methods for other classes
"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """Parent class tu use in other classes
    Attributes:
          created_at: input attribute
          updated_at: input attribute
          __str__: input attribute
          save: input attribute
          to_dict: input attribute
    """

    def __str__(self):
        """method that prints"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                       self.id, self.__dict__))

    def save(self):
        """
        method that updates the public instance
        attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        """
        ins_dict = dict(self.__dict__)
        ins_dict['created_at'] = self.__dict__['created_at'].isoformat()
        ins_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        ins_dict['__class__'] = self.__class__.__name__
        return (ins_dict)

    def __init__(self, *args, **kwargs):
        """
        inistialization
        args:
            *args: input value
            ***kwargs: input value
        """
        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['crated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

        for i, j in kwargs.items():
            if i != '__class__':
                setattr(self, i, j)
            else:
                self.id = str(uuid.uuid4())
                self.creted_at = datetime.now()
                self.updated_at = datetime.now()
                models.storage.new(self)
