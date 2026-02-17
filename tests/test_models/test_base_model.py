#!/usr/bin/python3
"""
Unittest for the BaseModel class
"""
import unittest
import os
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up for the tests"""
        self.my_model = BaseModel()

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init(self):
        """Test initialization of BaseModel"""
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertTrue(hasattr(self.my_model, "id"))
        self.assertTrue(hasattr(self.my_model, "created_at"))
        self.assertTrue(hasattr(self.my_model, "updated_at"))

    def test_save_updates_file(self):
        """Test that save updates the file"""
        self.my_model.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_to_dict(self):
        """Test the to_dict method"""
        model_dict = self.my_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.my_model.id)

if __name__ == '__main__':
    unittest.main()