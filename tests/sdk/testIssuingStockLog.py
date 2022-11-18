import starkinfra
from unittest import TestCase, main
from tests.utils.user import exampleProject

starkinfra.user = exampleProject


class TestIssuingStockLogQuery(TestCase):

    def test_success(self):
        logs = starkinfra.issuingstock.log.query(limit=10)
        for log in logs:
            self.assertEqual(log.id, str(log.id))


class TestIssuingStockLogGet(TestCase):

    def test_success(self):
        logs = starkinfra.issuingstock.log.query(limit=1)
        log = starkinfra.issuingstock.log.get(id=next(logs).id)
        self.assertEqual(log.id, str(log.id))


if __name__ == '__main__':
    main()
