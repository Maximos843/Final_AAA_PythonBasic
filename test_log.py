import unittest
from order import log
from unittest.mock import patch


class TestLog(unittest.TestCase):
    @patch('builtins.print')
    def test_output_log(self, print_mock):
        """Функция тестирующая возможность корректного запуска декоратора"""
        @log('Testing: {}, {}!')
        def test_func(testing: str):
            return 'Testing action'

        test_func('testing')
        self.assertTrue(print_mock.called)
