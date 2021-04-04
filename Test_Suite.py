#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest


# In[2]:
from Test_base import *
from Test_filter import *
#from Test_Scripts.Test_base import *
#from Test_Scripts.Test_filter import *


# In[3]:


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    
    suite.addTest(unittest.makeSuite(Test_base_functions))
    suite.addTest(unittest.makeSuite(Test_filter))

    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()


# In[ ]:




