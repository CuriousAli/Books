from unittest import TestCase

from Service.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(6, 13, '+')
        self.assertEqual(19, result)


    def test_minus(self):
        result = operations(10, 5, '-')
        self.assertEqual(5, result)


    def test_multipy(self):
        result = operations(10, 5, '*')
        self.assertEqual(50, result)