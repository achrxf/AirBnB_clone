#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""

import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.user = User()

    def test_instance_creation(self):
        """Test User instance creation."""
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        """Test User attributes."""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_str_representation(self):
        """Test __str__ method of User."""
        expected_str = "[User] ({}) {}".format(
            self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method of User."""
        user_dict = self.user.to_dict()

        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)

    def test_save_method(self):
        """Test save method of User."""
        old_updated_at = self.user.updated_at
        self.user.save()
        new_updated_at = self.user.updated_at

        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertTrue(isinstance(new_updated_at, datetime))

    def tearDown(self):
        """Tear down the test environment."""
        del self.user


if __name__ == '__main__':
    unittest.main()
