#   Fixtures can also be used to load data
import pytest
from PytestDemo.BaseClass import BaseClass


#   Show case of how we can load data using fixtures
#   as well as inherit logging class
@pytest.mark.usefixtures("data")
class TestExample2(BaseClass):
    def test_loadData(self, data):
        log = self.getLogger()
        log.info(data[1])
