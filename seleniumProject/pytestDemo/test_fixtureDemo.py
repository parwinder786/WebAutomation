import pytest

# @pytest.fixture()
# def setup():
#     print("i will be executing first")
#     yield    # it is used as teardown method, will be executed in last
#     print('i will be executed in last ')

def test_fixturedemo(setup):    # call the fixture, it will execute the setup method before executing its method
    print("i will execute steps in fixturEdEMO METHOD")