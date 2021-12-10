import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase): #inherits from unittest.TestCase
    """Tests for 'name function.py'"""

    def test_first_last_name(self): #any method that starts with "test_" will be run automatically
        """Do names like 'Jimi Hendrix' work?"""
        formatted_name = get_formatted_name('jimi', 'hendrix')
        self.assertEqual(formatted_name, 'Jimi Hendrix')

    def test_first_middle_last_name(self): #any method that starts with "test_" will be run automatically
        """Do names like 'Jimi Ebenezer Hendrix' work?"""
        formatted_name = get_formatted_name('jimi', 'hendrix', 'ebenezer')
        self.assertEqual(formatted_name, 'Jimi Ebenezer Hendrix')

unittest.main() #This tells Python to run the tests in this file