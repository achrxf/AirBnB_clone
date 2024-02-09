#!/usr/bin/python3
"""BaseModel."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel."""
    def __init__(self, *args, **kwargs):
        """A BaseModel."""
        ti_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if len(kwargs) != 0:
            for keyy, val in kwargs.items():
                if keyy == "created_at" or keyy == "updated_at":
                    self.__dict__[keyy] = datetime.strptime(val, ti_form)
                else:
                    self.__dict__[keyy] = val
        else:
            models.storage.new(self)

    def save(self):
        """Update the public instance."""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary."""
        in_dict = self.__dict__.copy()
        in_dict["__class__"] = self.__class__.__name__
        in_dict["created_at"] = self.created_at.isoformat()
        in_dict["updated_at"] = self.updated_at.isoformat()
        return in_dict

    def __str__(self):
        """Representation of the BaseModel instance."""
        cl_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_name, self.id, self.__dict__)
