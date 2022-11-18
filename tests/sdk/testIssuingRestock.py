import starkinfra
from unittest import TestCase, main
from datetime import date, timedelta
from tests.utils.user import exampleProject
from tests.utils.issuingRestock import generateExampleRestocksJson

starkinfra.user = exampleProject


class TestIssuingRestockQuery(TestCase):

    def test_success(self):
        restocks = starkinfra.issuingrestock.query(
            after=date.today() - timedelta(days=100),
            before=date.today(),
        )
        for restock in restocks:
            self.assertEqual(restock.id, str(restock.id))


class TestIssuingRestockGet(TestCase):

    def test_success(self):
        restocks = starkinfra.issuingrestock.query(limit=1)
        restock = starkinfra.issuingrestock.get(id=next(restocks).id)
        self.assertEqual(restock.id, str(restock.id))


class TestIssuingRestockPost(TestCase):

    def test_success(self):
        example_restocks = generateExampleRestocksJson(n=5)
        restock = starkinfra.issuingrestock.create(example_restocks)
        self.assertEqual(restock.id, str(restock.id))
        print(restock)


if __name__ == '__main__':
    main()
