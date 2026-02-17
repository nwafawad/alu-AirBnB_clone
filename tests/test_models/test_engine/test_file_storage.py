#!/usr/bin/python3
"""
Unittest for the FileStorage class
"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.file_path = "file.json"

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        # Reset storage
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """Test the all method"""
        self.assertIsInstance(self.storage.all(), dict)
        # Create a new object and verify it's in the dictionary
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_new(self):
        """Test the new method"""
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_save(self):
        """Test the save method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        # Verify content
        with open(self.file_path, "r") as f:
            content = json.load(f)
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.assertIn(key, content)

    def test_reload(self):
        """Test the reload method"""
        # Save an object
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        
        # Clear storage and reload
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

if __name__ == '__main__':
    unittest.main()