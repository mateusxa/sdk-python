from random import randint
from starkinfra import IssuingRestock, issuingstock



example_restock = IssuingRestock(
    count=1000,
    stockId="6526579068895232"
)


def generateExampleRestocksJson(holder, n=1):
    restocks = []
    for _ in range(n):
        example_restock.count = randint(1, 1000)
        example_restock.stockId = next(issuingstock.query(limit=1)).id
        restock.append(deepcopy(example_restock))
    return restocks
