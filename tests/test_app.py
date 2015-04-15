import unittest
from unittest.mock import MagicMock
from cli.app import App
from cli.command import Command
from cli.flag import Flag

class TestAppCommandWithNoFlags(unittest.TestCase):
    def setUp(self):
        self.app = App(name='app name', description='app description')
        self.app.print_help = MagicMock()
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

    def test_app_command_executed_with_no_flags(self):
        self.app.run(['command.py', 'test_command', '-testflag', 'flagvalue'])
        self.assertEqual(self.command.execute.call_args[0][0].get('test'), None, 'command is executed with an empty context')

class TestAppCommandWithFlags(TestAppCommandWithNoFlags):
    def setUp(self):
        super(TestAppCommandWithFlags, self).setUp()
        self.command.flags = [Flag('flag1', 'flag 1 desc'), Flag('flag2', 'flag 2 desc')]

    def test_cli_args_does_not_include_flags(self):
        self.app.run(['command.py', 'test_command', '-flag1', 'flag 1 value', '-flag2', 'flag 2 value'])
        context = self.command.execute.call_args[0][0]

        self.assertEqual(context.get('flag1'), 'flag 1 value', 'the first flag is the proper value')
        self.assertEqual(context.get('flag2'), 'flag 2 value', 'the second flag is the proper value')

if __name__ == '__main__':
    unittest.main()
