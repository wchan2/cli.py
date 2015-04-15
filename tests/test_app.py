import unittest
from unittest.mock import MagicMock
from cli.app import App
from cli.command import Command

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App(name='app name', description='app description')
        self.command = Command('test_command', 'test description')
        self.command.execute = MagicMock(return_value=None)
        self.app.command(self.command)

    def tearDown(self):
        self.app = None
        self.command = None

    def test_app_name(self):
        self.assertEquals(self.app.name, 'app name', 'app name is the proper value')

    def test_app_description(self):
        self.assertEquals(self.app.description, 'app description', 'app description is the proper value')

    def test_app_commands(self):
        self.assertEquals(self.app.commands[0], self.command, 'the command is saved in the app\'s command list')

    def test_app_run_with_found_command(self):
        self.app.run(['command.py', 'test_command'])
        self.assertTrue(self.command.execute.called, 'command is found and executed')

    def test_app_run_with_unfound_command(self):
        with self.assertRaises(SystemExit):
            self.app.run(['command.py', 'nonexistent_command'])

    def test_app_run_with_less_than_2_arguments(self):
        with self.assertRaises(SystemExit):
            self.app.run([])

if __name__ == '__main__':
    unittest.main()
