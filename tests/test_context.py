import unittest
from unittest.mock import MagicMock
from cli.context import Context

class TestContext(unittest.TestCase):
    def setUp(self):
        self.context = Context()
        self.context.set('key', 'value')

    def tearDown(self):
        self.context = None

    def test_set(self):
        self.assertEqual(self.context.values['key'], 'value', 'sets the value for the key')

    def test_get_returns_none_for_non_existent_key(self):
        self.assertEqual(self.context.get('nonexistent'), None, 'returns none when the value for the key doesn\'t exist')

    def test_get_returns_value_for_existing_key(self):
        self.assertEqual(self.context.get('key'), 'value', 'returns the value stored within a given key')



if __name__ == '__main__':
    unittest.main()
