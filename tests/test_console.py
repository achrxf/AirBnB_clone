#!/usr/bin/python3
"""The console tests."""

import os
import sys
import unittest
from unittest.mock import create_autospec, patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    """Class to test the console."""

    def setUp(self):
        """Set up test environment."""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up after tests."""
        pass

    def test_help_command(self):
        """Test the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            help_output = f.getvalue()
            ex = ['EOF', 'all', 'count', 'create',
                  'destroy', 'help', 'quit', 'show', 'update']
            for command in ex:
                self.assertIn(command, help_output)

    def test_create_command(self):
        """Test the create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertIn("** class name missing **", f.getvalue())

    def test_show_command_missing_class(self):
        """Test the show command with missing class."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertIn("** class name missing **", f.getvalue())

    def test_show_command_missing_id(self):
        """Test the show command with missing ID."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertIn("** instance id missing **", f.getvalue())

    def test_show_command_no_instance_found(self):
        """Test the show command with no instance found."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel 12345")
            self.assertIn("** no instance found **", f.getvalue())

    def test_all_command_no_class(self):
        """Test the all command with no class."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            self.assertIn("** class doesn't exist **", f.getvalue())

    def test_all_command_invalid_class(self):
        """Test the all command with invalid class."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all MyModel")
            self.assertIn("** class doesn't exist **", f.getvalue())

    def test_destroy_command_missing_class(self):
        """Test the destroy command with missing class."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertIn("** class name missing **", f.getvalue())

    def test_destroy_command_missing_id(self):
        """Test the destroy command with missing ID."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertIn("** instance id missing **", f.getvalue())

    def test_destroy_command_no_instance_found(self):
        """Test the destroy command with no instance found."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 12345")
            self.assertIn("** no instance found **", f.getvalue())

    def test_update_command_missing_class(self):
        """Test the update command with missing class."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertIn("** class name missing **", f.getvalue())

    def test_update_command_missing_id(self):
        """Test the update command with missing ID."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertIn("** instance id missing **", f.getvalue())

    def test_update_command_no_instance_found(self):
        """Test the update command with no instance found."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 12345")
            self.assertIn("** no instance found **", f.getvalue())

    def test_quit_command(self):
        """Test the quit command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_count_command_missing_class(self):
        """Test the count command with missing class."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count BaseModel")
            self.assertIn("0", f.getvalue())

    def test_count_command_valid_class(self):
        """Test the count command with valid class."""
        # Create instances to count
        BaseModel().save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count BaseModel")
            self.assertIn("1", f.getvalue())

    def test_invalid_command(self):
        """Test an invalid command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("invalid_command")
            self.assertIn("*** Unknown syntax:", f.getvalue())


if __name__ == '__main__':
    unittest.main()
