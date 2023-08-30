#   With this file name, it can be used as a global fixture for all files with test_
#   Only use this if fixture is used between multiple files
import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield  # this will run last
    print("executed last")


#   To load/pass data using fixtures
@pytest.fixture(scope="class")
def data():
    print("user profile is being created")
    return ["timothy", "toribio", "rahulshetyacademy.com"]


#   example of parametrised fixture
@pytest.fixture(params=[("chrome", "multi"), "firefox", "IE"])
def crossBrowser(request):
    return request.param
