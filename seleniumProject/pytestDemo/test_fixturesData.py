import pytest

from pytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad") #dataLoad is coming from conftest file, will ve available to use in class method
class TestExample2(BaseClass): #BaseClass is parent class, inhertired in this class TE2

    def test_editProfile(self, dataLoad):
        log = self.getLogger()  # it will return logger from parent class
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        print(dataLoad[2])

