import starkinfra
from unittest import TestCase, main
from datetime import date, timedelta
from tests.utils.user import exampleProject

starkinfra.user = exampleProject


class TestIssuingDesignQuery(TestCase):

    def test_success(self):
        designs = starkinfra.issuingdesign.query(
            after=date.today() - timedelta(days=100),
            before=date.today(),
        )
        for design in designs:
            self.assertEqual(design.id, str(design.id))


class TestIssuingDesignGet(TestCase):

    def test_success(self):
        designs = starkinfra.issuingdesign.query(limit=1)
        design = starkinfra.issuingdesign.get(id=next(designs).id)
        self.assertEqual(design.id, str(design.id))


class TestDesignPdfGet(TestCase):

    def test_success(self):
        designs = starkbank.design.query()
        design_id = next(designs).id
        pdf = starkbank.design.pdf(design_id)
        self.assertGreater(len(pdf), 1000)

if __name__ == '__main__':
    main()
