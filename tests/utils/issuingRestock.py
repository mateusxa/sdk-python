from random import randint
from starkinfra import IssuingRestock, issuingstock



example_restock = IssuingRestock(
    count=1000,
    stockId="6526579068895232"
)


def generateExampleRestocksJson():
    example_restock.count = randint(1, 1000)
    example_restock.stockId = next(issuingstock.query(limit=1)).id
    return example_restock
