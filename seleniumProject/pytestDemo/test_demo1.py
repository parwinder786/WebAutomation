# Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only


import pytest



@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")
#
def test_crossBrowser(crossBrowser): #calling the browser from conftest file, it will run 3 time
    print(crossBrowser[1]) #takes the index 1 of conftest file defined values


