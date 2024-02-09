#!/usr/bin/python3
"""FileStorage."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent a storage engine."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj."""
        ob_cl_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ob_cl_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        all_dict = FileStorage.__objects
        ob_dict = {obj: all_dict[obj].to_dict() for obj in all_dict.keys()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(ob_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                ob_dict = json.load(file)
                for ob in ob_dict.values():
                    cl_name = ob["__class__"]
                    del ob["__class__"]
                    self.new(eval(cl_name)(**ob))
        except FileNotFoundError:
            return
