import starkinfra
from unittest import TestCase, main
from tests.utils.user import exampleProject

starkinfra.user = exampleProject


class TestIssuingPurchaseQuery(TestCase):

    def test_success(self):
        purchases = starkinfra.issuingpurchase.query(limit=10)
        for purchase in purchases:
            self.assertEqual(purchase.id, str(purchase.id))


class TestIssuingPurchaseGet(TestCase):

    def test_success(self):
        purchases = starkinfra.issuingpurchase.query(limit=1)
        purchase = starkinfra.issuingpurchase.get(id=next(purchases).id)
        self.assertEqual(purchase.id, str(purchase.id))


if __name__ == '__main__':
    main()
