from n26.api import GET
from tests.test_api_base import N26TestBase, mock_api


class BalanceTest(N26TestBase):

    @mock_api(method=GET, response_file="balance.json")
    def test_balance_ok(self):
        self._underTest.get_balance()
