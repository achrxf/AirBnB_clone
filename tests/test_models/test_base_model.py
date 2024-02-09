#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.base_model = BaseModel()

    def test_instance_creation(self):
        """Test BaseModel instance creation."""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_attributes(self):
        """Test BaseModel attributes."""
        self.assertTrue(isinstance(self.base_model.id, str))
        self.assertTrue(isinstance(self.base_model.created_at, datetime))
        self.assertTrue(isinstance(self.base_model.updated_at, datetime))

    def test_str_representation(self):
        """Test __str__ method of BaseModel."""
        expected_str = "[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method of BaseModel."""
        base_model_dict = self.base_model.to_dict()

        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(base_model_dict['created_at'], str)
        self.assertIsInstance(base_model_dict['updated_at'], str)

    def test_save_method(self):
        """Test save method of BaseModel."""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at

        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertTrue(isinstance(new_updated_at, datetime))

    def tearDown(self):
        """Tear down the test environment."""
        del self.base_model


if __name__ == '__main__':
    unittest.main()
