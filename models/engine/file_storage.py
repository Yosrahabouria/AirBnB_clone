#!/usr/bin/python3
"""Converting, reading and interpreating a json file"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """Representationg abstract storage engine
    Attributes:
        file_path (str): The name of the file to save objects.
        objects_dict (dict): A dictionary of instantiated objects.
    """
    file_path = "file.json"
    objects_dict = {}

    def all(self):
        """Returns the objects dictionary."""
        return FileStorage.objects_dict

    def new(self, obj):
        """Sets the object in the dictionary."""
        class_name = obj.__class__.__name__
        FileStorage.objects_dict["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """Saving method."""
        serialized_objects = {key: value.to_dict() for key, value in FileStorage.objects_dict.items()}
        with open(FileStorage.file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """reload method"""
        try:
            with open(FileStorage.file_path) as file:
                loaded_objects = json.load(file)
                for value in loaded_objects.values():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            return
