#!/usr/bin/python3
"""
Module file_storage
Defines the FileStorage class for serializing and deserializing instances.
"""
import json
import os


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file exists).
        """
        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                    obj_dict = json.load(f)
                
                from models.base_model import BaseModel
                # As you add more classes (User, State, etc.), add them here
                classes = {"BaseModel": BaseModel}

                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    if class_name in classes:
                        self.new(classes[class_name](**value))
            except Exception:
                pass