#!/usr/bin/python3
"""test file  console"""

import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch

class TestHBNBCommand(unittest.TestCase):
    """Class for testing"""
    def setUp(self):
        """to initialize"""
        self.hbnb_console = HBNBCommand()

    def tearDown(self):
        """Reloading of storage"""
        storage.reload()
            
    def capture_output(self, command):
        """Execution method"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_console.onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_quit_command(self):
        """Test of quit command"""
        result = self.capture_output('quit')
        self.assertEqual(result, "")

    def test_create_command(self):
        """Test of creation method"""
        result = self.capture_output('create BaseModel')
        self.assertIn("{}".format(self.hbnb_console.classes["BaseModel"]), result)

    def test_show_command(self):
        """Test of showing command"""
        instance_id = None
        with patch('builtins.input', return_value='create BaseModel'):
            self.hbnb_console.onecmd('create BaseModel')
            instance_id = list(storage.all().keys())[0]

        result = self.capture_output('show BaseModel {}'.format(instance_id))
        self.assertIn(instance_id, result)

if __name__ == '__main__':
    unittest.main()
