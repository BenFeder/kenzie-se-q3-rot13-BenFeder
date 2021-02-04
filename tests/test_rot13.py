#!/usr/bin/env python
"""
Unit tests for rot13

Students should not modify this file.
"""

__author__ = 'pydan'

import sys
import unittest
import importlib
import subprocess

# suppress __pycache__ and .pyc files
sys.dont_write_bytecode = True

# Kenzie devs: change this to 'soln.rot13' to test solution
PKG_NAME = 'rot13'


class TestRot13(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Performs module import and suite setup at test-runtime."""
        # check for python3
        cls.assertGreaterEqual(cls, sys.version_info[0], 3)
        # this will import the module to be tested
        cls.module = importlib.import_module(PKG_NAME)

    def test_flake8(self):
        """Checking for PEP8/flake8 compliance."""
        result = subprocess.run(['flake8', self.module.__file__])
        self.assertEqual(result.returncode, 0)

    def test_author_string(self):
        """Checking for author string."""
        self.assertIsNotNone(self.module.__author__)
        self.assertNotEqual(
            self.module.__author__, "???",
            "Author string is not completed"
        )

    def test_encode_basic(self):
        """Check if basic lowercase encoding/decoding works."""
        rotate = self.module.rotate
        encoded = rotate('hello')
        decoded = rotate(encoded)
        self.assertEqual(encoded, 'uryyb')
        self.assertEqual(decoded, 'hello')

    def test_encode_mixed(self):
        """Check if mixed case encoding works."""
        rotate = self.module.rotate
        encoded = rotate('HelLo')
        decoded = rotate(encoded)
        self.assertEqual(encoded, 'UryYb')
        self.assertEqual(decoded, 'HelLo')

    def test_proud_caesar(self):
        """Check if transcoding works with non-alpha characters."""
        rotate = self.module.rotate

        encoded = rotate("You've made Caesar 100% proud.")
        decoded = rotate(encoded)
        self.assertEqual(encoded, "Lbh'ir znqr Pnrfne 100% cebhq.")
        self.assertEqual(decoded, "You've made Caesar 100% proud.")


if __name__ == '__main__':
    unittest.main()
