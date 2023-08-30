import pytest


#   This tells pytest to only run these methods, they are 'marked' if they have this
#   on top of the method. To run in cmd >py.test -m smoke -v -s
@pytest.mark.smoke
def test_firstProg():
    msg = "hello"
    assert msg == "hi", "Test Failed : Strings don't match!"


#   In the case that a function is a pre-requisite to other stuff but
#   you dont want to see it in the report, we can use mark xfail
@pytest.mark.xfail
def test_SecondProgram():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition does not match!"


#   To skip a test,use skip mark
@pytest.mark.skip
def test_creditcardOCBC():
    print("This is the OTHER")


