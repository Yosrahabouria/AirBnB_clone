#!/usr/bin/python3
"""File storage in python model"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """Représente un moteur de stockage abstrait.
    Attributs:
        __file_path (str): Le nom du fichier pour sauvegarder les objets.
        __objects (dict): Un dictionnaire des objets instanciés.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retourne le dictionnaire __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Définit dans __objects obj avec la clé <nom_classe_obj>.id."""
        nom_classe = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(nom_classe, obj.id)] = obj

    def save(self):
        """Sérialise __objects dans le fichier JSON __file_path."""
        objets_serializes = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objets_serializes, f)

    def reload(self):
        """Désérialise le fichier JSON __file_path vers __objects, s'il existe."""
        try:
            with open(FileStorage.__file_path) as f:
                objets_charges = json.load(f)
                for v in objets_charges.values():
                    classe = v["__class__"]
                    del v["__class__"]
                    self.new(eval(classe)(**v))
        except FileNotFoundError:
            return
