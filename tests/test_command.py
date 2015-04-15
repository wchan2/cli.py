import unittest
from unittest.mock import MagicMock, Mock
from cli.command import Command

class TestCommand(unittest.TestCase):
    def setUp(self):
        self.fake_context = Mock()
        self.fake_action = MagicMock()

        self.command = Command('test_command', 'test description')
        self.command(self.fake_action)

    def tearDown(self):
        self.command = None
        self.fake_context = None

    def test_command_name(self):
        self.assertEqual(self.command.name, 'test_command', 'command name is the proper value')

    def test_command_description(self):
        self.assertEqual(self.command.description, 'test description', 'command description is the proper value')

    def test_call_sets_action(self):
        self.assertEqual(self.fake_action, self.command.action, '.action is set by calling the command object')

    def test_execute_calls_action_with_proper_context(self):
        self.command.execute(self.fake_context)
        self.command.action.assert_called_with(self.fake_context)

if __name__ == '__main__':
    unittest.main()
