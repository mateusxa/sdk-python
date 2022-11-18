from random import randint
from starkinfra import IssuingEmbossingRequest, issuingstock



example_embossingrequest = IssuingEmbossingRequest(
    count=1000,
    stockId="6526579068895232"
)


def generateExampleEmbossingRequestsJson(holder, n=1):
    embossingrequests = []
    for _ in range(n):
        example_embossingrequest.count = randint(1, 1000)
        example_embossingrequest.stockId = next(issuingstock.query(limit=1)).id
        embossingrequest.append(deepcopy(example_embossingrequest))
    return embossingrequests
