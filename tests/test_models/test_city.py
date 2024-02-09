#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""

import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.city = City()

    def test_instance_creation(self):
        """Test City instance creation."""
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        """Test City attributes."""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_str_representation(self):
        """Test __str__ method of City."""
        expected_str = "[City] ({}) {}".format(
            self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method of City."""
        city_dict = self.city.to_dict()

        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)

    def test_save_method(self):
        """Test save method of City."""
        old_updated_at = self.city.updated_at
        self.city.save()
        new_updated_at = self.city.updated_at

        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertTrue(isinstance(new_updated_at, datetime))

    def tearDown(self):
        """Tear down the test environment."""
        del self.city


if __name__ == '__main__':
    unittest.main()
