#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
from models.review import Review
from models.base_model import BaseModel


import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.review = Review()

    def test_instance_creation(self):
        """Test Review instance creation."""
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        """Test Review attributes."""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_str_representation(self):
        """Test __str__ method of Review."""
        expected_str = "[Review] ({}) {}".format(
            self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method of Review."""
        review_dict = self.review.to_dict()

        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)

    def test_save_method(self):
        """Test save method of Review."""
        old_updated_at = self.review.updated_at
        self.review.save()
        new_updated_at = self.review.updated_at

        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertTrue(isinstance(new_updated_at, datetime))

    def tearDown(self):
        """Tear down the test environment."""
        del self.review


if __name__ == '__main__':
    unittest.main()
