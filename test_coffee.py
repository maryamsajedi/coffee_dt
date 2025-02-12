import unittest
import numpy as np
from dt_model import Model

excepted = [
 [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
 [1., 1., 1., 1., 1., 1., 1., 1., 1., 0.],
 [1., 1., 1., 1., 1., 1., 1., 1., 0., 0.],
 [1., 1., 1., 1., 1., 1., 1., 0., 0., 0.],
 [1., 1., 1., 1., 1., 1., 0., 0., 0., 0.,],
 [1., 1., 1., 1., 1., 0., 0., 0., 0., 0.,],
 [1., 1., 1., 1., 0., 0., 0., 0., 0., 0.,],
 [1., 1., 1., 0., 0., 0., 0., 0., 0., 0.,],
 [1., 1., 0., 0., 0., 0., 0., 0., 0., 0.,],
 [1., 0., 0., 0., 0., 0., 0., 0., 0., 0.,]
]
# This is the idea
class TestCoffee(unittest.TestCase):
    def test_coffee(self):
        test_cases = [
            {"name": 'test1',
            "input": {},
            "expected":excepted},

            {"name": 'test2',
            "input": {   
            },
            "expected": excepted},  
        ]

        for case in test_cases:
            actual = Model(input)
            self.assertEqual(actual, case['expected'], msg=f"Test {case['name']} failed. Expected {case['expected']} but got {actual}")