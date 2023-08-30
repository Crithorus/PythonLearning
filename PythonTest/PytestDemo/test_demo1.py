#   Any pytest file should start with test_ or end with _test
#   pytest method names should start with test
#   Any code should be wrapped in method only
#   For console , -v shows more details -s prints console log
#   IMPORTANT: Can't have 2 methods with the same name, otherwise it will overwrite the
#   previous method
import pytest


#   to test a single file, we need to type the file name inside cmd (eg >py.test test_demo1.py

#   We can can also command it to test methods that contains a specfic name
#   example would be test_creditcard1 & test_creditcard2. in cmd, it will look like:
#   >py.test -k creditcard -v -s
def test_firstProgram():
    print("Hello")


@pytest.mark.smoke
def test_secondProgram():
    print("Good Morning")


def test_creditcard1():
    print("this is part 1")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])

