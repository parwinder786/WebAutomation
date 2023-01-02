import pytest


@pytest.fixture(scope="class") #scope = class means it will run only once before the class and end of class teardown method
def setup():
    print("I will be executing first")
    yield
    print(" I will execute last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul","Shetty","rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome","Rahul","shetty"), ("Firefox","singh"), ("IE","SS")]) #3 times test will run
def crossBrowser(request): #request instance linked to fixture, 1st time chrome will be picked
    return request.param
