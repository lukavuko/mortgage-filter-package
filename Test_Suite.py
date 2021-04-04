#!/usr/bin/env python
# coding: utf-8

import unittest
from tests.test_base import *
from tests.test_filter import *

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    
    suite.addTest(unittest.makeSuite(Test_base_functions))
    suite.addTest(unittest.makeSuite(Test_filter))

    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()
