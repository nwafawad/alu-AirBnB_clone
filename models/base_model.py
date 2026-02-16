#!/usr/bin/python3
"""
Module base_model
Defines the BaseModel class which will serve as the base for all other classes.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class defines all common attributes/methods for other classes.
    """

    def __init__(self):
        """
        Initializes the public instance attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the instance.
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance.
        """
        # Create a copy of the dictionary to avoid modifying the original
        new_dict = self.__dict__.copy()
        # Add the __class__ key
        new_dict["__class__"] = self.__class__.__name__
        # Convert datetime objects to ISO format strings
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict