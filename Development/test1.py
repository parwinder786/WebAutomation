#----------------testing----------------

import unittest
import pytest
import main

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        '''Hi, this is test1'''
        para = 10
        result = main.do_stuff(para)
        self.assertEquals(result,15)

    def test_do_stuff2(self):
        para = 'sheuu'
        result = main.do_stuff(para)
        #self.assertTrue(isinstance(result, ValueError)) # to see if its returning value error
        self.assertIsInstance(result, ValueError) # improved code

    def test_do_stuff3(self):
        para = None
        result = main.do_stuff(para)
        self.assertEquals(result, 'please enter number')

    def test_do_stuff4(self):
        para = ''
        result = main.do_stuff(para)
        self.assertEquals(result, 'please enter number')


#unittest.main() #main meaning here to run all the tests, it has nothing relation with other main file
#other way of running the test file, if there more test files, then its useful
if __name__ == '__main__':
    unittest.main()
