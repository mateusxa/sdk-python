import starkinfra
from unittest import TestCase, main
from datetime import date, timedelta
from tests.utils.user import exampleProject
from tests.utils.issuingEmbossingRequest import generateExampleEmbossingRequestsJson

starkinfra.user = exampleProject


class TestIssuingEmbossingRequestQuery(TestCase):

    def test_success(self):
        embossingrequests = starkinfra.issuingembossingrequest.query(
            after=date.today() - timedelta(days=100),
            before=date.today(),
        )
        for embossingrequest in embossingrequests:
            self.assertEqual(embossingrequest.id, str(embossingrequest.id))


class TestIssuingEmbossingRequestGet(TestCase):

    def test_success(self):
        embossingrequests = starkinfra.issuingembossingrequest.query(limit=1)
        embossingrequest = starkinfra.issuingembossingrequest.get(id=next(embossingrequests).id)
        self.assertEqual(embossingrequest.id, str(embossingrequest.id))


class TestIssuingEmbossingRequestPost(TestCase):

    def test_success(self):
        example_embossingrequests = generateExampleEmbossingRequestsJson(n=5)
        embossingrequest = starkinfra.issuingembossingrequest.create(example_embossingrequests)
        self.assertEqual(embossingrequest.id, str(embossingrequest.id))
        print(embossingrequest)


if __name__ == '__main__':
    main()
