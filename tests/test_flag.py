import unittest
from unittest.mock import MagicMock
from cli.flag import Flag

class TestFlagWithoutDefault(unittest.TestCase):
    def setUp(self):
        self.flag = Flag(name='flag name', description='flag description')

    def tearDown(self):
        self.flag = None

    def test_flag_name(self):
        self.assertEqual(self.flag.name, 'flag name', 'flag name is the proper value')

    def test_flag_description(self):
        self.assertEqual(self.flag.description, 'flag description', 'flag description is the proper value')

    def test_flag_default_value(self):
        self.assertEqual(self.flag.value, None, 'the default value is set to none')

class TestFlagWithDefault(TestFlagWithoutDefault):
    def setUp(self):
        self.flag = Flag('flag name', 'flag description', value='default value')

    def tearDown(self):
        self.flag = None

    def test_flag_default_value(self):
        self.assertEqual(self.flag.value, 'default value', 'the flag\'s default value is set to the default value')

if __name__ == '__main__':
    unittest.main()
