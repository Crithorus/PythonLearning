#   If i need to execute a code PREREQUISITE to the real test

import pytest


# @pytest.fixture()
# def setup():
#     print("I will be executed first")
#     yield  # this will run last
#     print("executed last")


#   In order to let it know that it will run after the fixture, pass the method to the param
# def test_fixtureDemo(setup):
#     print("executed after fixture")


#   if you have multiple methods using the same fixture, wrap it in a class
@pytest.mark.usefixtures("data")
class TestExample:
    def test_fixtureDemo1(self, data):
        print("executed after fixture1")

    def test_fixtureDemo2(self):
        print("executed after fixture2")

    def test_fixtureDemo3(self):
        print("executed after fixture3")
