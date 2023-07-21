#!/usr/bin/env python3
'''
Import unittest framework and the Calculator class
we defined.
'''

from Calculator import Calculator

'''
Test cases are created by subclassing unittest.TestCase
'''
class TestCalculator():

    def test_add(self):
        self.calculator = Calculator()
        add_result = self.calculator.add(1, 2)
        assert add_result == 3


    def test_subtract(self):
        self.calculator = Calculator()
        subtract_result = self.calculator.subtract(1, 1)
        assert subtract_result == 0



