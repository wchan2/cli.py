
import unittest
from test_app import TestAppCommandWithNoFlags, TestAppCommandWithFlags
from test_command import TestCommand

if __name__ == '__main__':
    test_loader = unittest.TestLoader()
    suites = unittest.TestSuite(map(
        lambda test_case: test_loader.loadTestsFromTestCase(test_case),
        [TestAppCommandWithNoFlags, TestAppCommandWithFlags, TestCommand])
    )
    unittest.TextTestRunner().run(suites)