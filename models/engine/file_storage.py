#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

<<<<<<< HEAD

class FileStorage():
    """Représente un moteur de stockage abstrait.
    Attributs:
        __file_path (str): Le nom du fichier pour sauvegarder les objets.
        __objects (dict): Un dictionnaire des objets instanciés.
=======
class FileStorage:
    """Representation of abstract storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects.
        __objects (dict): A dictionary of instantiated objects.
>>>>>>> 160f6a61c4f65e1c3d7361bc7f81265293cf2608
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the objects dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in objects """
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """Serializes objects into the JSON file path."""
        serialized_objects = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file path to objects"""
        try:
            with open(FileStorage.__file_path) as file:
                loaded_objects = json.load(file)
                for value in loaded_objects.values():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            return
