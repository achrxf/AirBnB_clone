#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestState_instantiation
    TestState_save
    TestState_to_dict
"""

import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.state = State()

    def test_instance_creation(self):
        """Test State instance creation."""
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        """Test State attributes."""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, "")

    def test_str_representation(self):
        """Test __str__ method of State."""
        expected_str = "[State] ({}) {}".format(
            self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method of State."""
        state_dict = self.state.to_dict()

        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)

    def test_save_method(self):
        """Test save method of State."""
        old_updated_at = self.state.updated_at
        self.state.save()
        new_updated_at = self.state.updated_at

        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertTrue(isinstance(new_updated_at, datetime))

    def tearDown(self):
        """Tear down the test environment."""
        del self.state


if __name__ == '__main__':
    unittest.main()
