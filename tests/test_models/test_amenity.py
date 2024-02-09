#!/usr/bin/python3
"""Defines unittests for models/amenity.py.

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.amenity = Amenity()

    def test_instance_creation(self):
        """Test Amenity instance creation."""
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes(self):
        """Test Amenity attributes."""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "")

    def test_str_representation(self):
        """Test __str__ method of Amenity."""
        expected_str = "[Amenity] ({}) {}".format(
            self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method of Amenity."""
        amenity_dict = self.amenity.to_dict()

        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)

    def test_save_method(self):
        """Test save method of Amenity."""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        new_updated_at = self.amenity.updated_at

        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertTrue(isinstance(new_updated_at, datetime))

    def tearDown(self):
        """Tear down the test environment."""
        del self.amenity


if __name__ == '__main__':
    unittest.main()
