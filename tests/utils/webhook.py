import starkbank
from uuid import uuid4


def generateExampleWebhook():
    return starkbank.Webhook(
        url="https://webhook.site/{uuid}".format(uuid=str(uuid4())),
        subscriptions=[
            "contract", "credit-note", "signer",
            "issuing-card", "issuing-invoice", "issuing-purchase",
            "pix-request.in", "pix-request.out", "pix-reversal.in", "pix-reversal.out",
        ],
    )
