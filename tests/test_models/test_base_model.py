#!/usr/bin/python3
"""
Unittest for the BaseModel class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up for the tests"""
        self.my_model = BaseModel()

    def test_init(self):
        """Test initialization of BaseModel"""
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertTrue(hasattr(self.my_model, "id"))
        self.assertTrue(hasattr(self.my_model, "created_at"))
        self.assertTrue(hasattr(self.my_model, "updated_at"))
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def test_str(self):
        """Test the __str__ method"""
        string = str(self.my_model)
        self.assertIn("[BaseModel]", string)
        self.assertIn(self.my_model.id, string)
        self.assertIn(str(self.my_model.__dict__), string)

    def test_save(self):
        """Test the save method"""
        old_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(old_updated_at, self.my_model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        model_dict = self.my_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.my_model.id)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()