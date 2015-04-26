
import unittest
from tests.test_app import TestAppCommandWithFlags, TestAppCommandWithNoFlags
from tests.test_command import TestCommand
from tests.test_flag import TestFlagWithoutDefault, TestFlagWithDefault
from tests.test_context import TestContext

if __name__ == '__main__':
    test_loader = unittest.TestLoader()
    suites = unittest.TestSuite(map(
        lambda test_case: test_loader.loadTestsFromTestCase(test_case),
        [
            TestAppCommandWithNoFlags,
            TestAppCommandWithFlags,
            TestCommand,
            TestFlagWithoutDefault,
            TestFlagWithDefault,
            TestContext
        ])
    )
    unittest.TextTestRunner().run(suites)