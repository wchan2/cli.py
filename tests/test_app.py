import unittest
from unittest.mock import Mock
from cli.app import App
from cli.command import Command
from cli.flag import Flag

class TestAppCommandWithNoFlags(unittest.TestCase):
    def setUp(self):
        self.app = App(name='app name', description='app description')

        self.command_mock_without_flags = Mock()
        self.command_mock_without_flags.execute = Mock(return_value=None)
        self.command_mock_without_flags.configure_mock(name='test_command', description='test description', flags=[])

        flag_mock = Mock()
        flag_mock.configure_mock(name='test_flag', description='flag_value')
        self.command_mock_with_flag = Mock()
        self.command_mock_with_flag.execute = Mock(return_value=None)
        self.command_mock_with_flag.configure_mock(name='test_command', description='test description', flags=[flag_mock])

        self.app.command(self.command_mock_without_flags)

        # mock the print statements so it doesn't actually output to stdout
        self.app.print_help = Mock()

    def tearDown(self):
        self.app = None
        self.command_mock_without_flags = None
        self.command_mock_with_flag = None

    def test_app_name(self):
        self.assertEqual(self.app.name, 'app name', 'app name is the proper value')

    def test_app_description(self):
        self.assertEqual(self.app.description, 'app description', 'app description is the proper value')

    def test_app_commands(self):
        self.assertEqual(self.app.commands[0], self.command_mock_without_flags, 'the command is saved in the app\'s command list')

    def test_app_create_parser(self):
        parsed_args = self.app.create_parser(self.command_mock_with_flag).parse_args(['test_command', '-test_flag', 'test flag value'])
        self.assertEqual(parsed_args.test_flag, 'test flag value', 'creates a parser that parses the correct value for a given flag')
        
    def test_app_run_with_found_command(self):
        self.app.run(['command.py', 'test_command'])
        self.assertTrue(self.command_mock_without_flags.execute.called, 'command is found and executed')

    def test_app_run_with_unfound_command(self):
        with self.assertRaises(SystemExit):
            self.app.run(['command.py', 'nonexistent_command'])

    def test_app_run_with_less_than_2_arguments(self):
        with self.assertRaises(SystemExit):
            self.app.run([])

    def test_app_command_executed_with_no_flags(self):
        self.app.run(['command.py', 'test_command'])
        self.assertTrue(self.command_mock_without_flags.execute.called, 'parses arguments')

class TestAppCommandWithFlags(TestAppCommandWithNoFlags):
    def setUp(self):
        super(TestAppCommandWithFlags, self).setUp()

        mock_flag_1 = Mock()
        mock_flag_2 = Mock()

        mock_flag_1.configure_mock(name='flag1', description='flag 1 desc')
        mock_flag_2.configure_mock(name='flag2', description='flag 2 desc')
        self.flag_mocks = [mock_flag_1, mock_flag_2]

    def test_cli_args_does_not_include_flags(self):
        with unittest.mock.patch.object(self.command_mock_with_flag, 'flags', self.flag_mocks):
            self.app.commands = [self.command_mock_with_flag]
            self.app.run(['command.py', 'test_command', '-flag1', 'flag 1 value', '--flag2', 'flag 2 value'])

            context = self.command_mock_with_flag.execute.call_args[0][0]

            self.assertEqual(context.get('flag1'), 'flag 1 value', 'the first flag is the proper value')
            self.assertEqual(context.get('flag2'), 'flag 2 value', 'the second flag is the proper value')

if __name__ == '__main__':
    unittest.main()
