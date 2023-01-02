#----------------testing----------------

import unittest
import pytest
import main

class TestMain(unittest.TestCase):

    def setUp(self):
        print('about to test a function') #setup is function of unitest, useful to set up before function

    def test_do_stuff(self):
        '''Hi, this is test'''
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

    def tearDown(self): #inbuilt unit test method
        print('cleaning up')


#unittest.main() #main meaning here to run all the tests, it has nothing relation with other main file
#other way of running the test file, if there more test files, then its useful
if __name__ == '__main__':
    unittest.main()
