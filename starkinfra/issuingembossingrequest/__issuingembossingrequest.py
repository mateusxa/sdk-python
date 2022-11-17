from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_date, check_datetime
from ..utils import rest


class IssuingEmbossingRequest(Resource):
    """# IssuingEmbossingRequest object
    The IssuingEmbossingRequest object displays the information of requested embossing orders in your Workspace.
    ## Parameters (required):
    - cardId [string]: Issuing card id to be embossed. ex "5656565656565656"
    - cardDesignId [string]: Issuing card design id to be embossed. ex "5656565656565656"
    - displayName1 [string]: card displayed name. ex: "ANTHONY STARK"
    - envelopeDesignId [string]: envelope design id to be embossed. ex "5656565656565656"
    - shippingCity [string]: shipping city. ex: "NEW YORK"
    - shippingCountryCode [string]: shipping country code. ex: "US"
    - shippingDistrict [string]: shipping district. ex: "NY"
    - shippingService [string]: shipping service. ex: "loggi"
    - shippingStateCode [string]: shipping state code. ex: "NY"
    - shippingStreetLine1 [string]: shipping street line 1. ex: "AVENUE OF THE AMERICAS"
    - shippingStreetLine2 [string]: shipping street line 2. ex: "AVENUE OF THE AMERICAS"
    - shippingTrackingNumber [string]: shipping tracking number. ex: "5656565656565656"
    ## Parameters (optional):
    - shippingZipCode [string]: shipping zip code. ex: "12345-678"
    - displayName2 [string]: card displayed name. ex: "ANTHONY STARK"
    - displayName3 [string]: card displayed name. ex: "ANTHONY STARK"
    - shippingPhone [string]: shipping phone. ex: "+5511999999999"
    - tags [list of string, default null]: tags to filter retrieved objects. ex: ["tony", "stark"]
    ## Attributes (return-only):
    - id [string, default null]: unique id returned when IssuingEmbossingRequest is created. ex: "5656565656565656"
    - fee [integer]: fee charged when IssuingEmbossingRequest is created. ex: 1000
    - status [string]: status of the IssuingEmbossingRequest. ex: "created"
    - subIssuerId [string]: id of the subIssuer. ex: "5656565656565656"
    - updated [datetime.datetime]: latest update datetime for the IssuingEmbossingRequest. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - created [datetime.datetime]: creation datetime for the IssuingEmbossingRequest. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(
        self, cardId, cardDesignId, displayName1, envelopeDesignId, shippingCity, 
        shippingCountryCode, shippingDistrict, shippingService, shippingStateCode, 
        shippingStreetLine1, shippingStreetLine2, shippingTrackingNumber, shippingZipCode=None,
        displayName2=None, displayName3=None, shippingPhone=None, tags=None, id=None, 
        fee=None, status=None, subIssuerId=None, created=None, updated=None
    ):
        Resource.__init__(self, id=id)

        self.cardId = cardId
        self.cardDesignId = cardDesignId
        self.displayName1 = displayName1
        self.envelopeDesignId = envelopeDesignId
        self.shippingCity = shippingCity
        self.shippingCountryCode = shippingCountryCode
        self.shippingDistrict = shippingDistrict
        self.shippingService = shippingService
        self.shippingStateCode = shippingStateCode
        self.shippingStreetLine1 = shippingStreetLine1
        self.shippingStreetLine2 = shippingStreetLine2
        self.shippingTrackingNumber = shippingTrackingNumber
        self.shippingZipCode = shippingZipCode
        self.displayName2 = displayName2
        self.displayName3 = displayName3
        self.shippingPhone = shippingPhone
        self.tags = tags
        self.fee = fee
        self.status = status
        self.subIssuerId = subIssuerId
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": IssuingEmbossingRequest, "name": "IssuingEmbossingRequest"}

def create(requests, user=None):
    """# Create IssuingEmbossingRequest
    Send a list of IssuingEmbossingRequest objects for creation at the Stark Infra API
    ## Parameters (required):
    - requests [list of IssuingEmbossingRequest objects]: list of IssuingEmbossingRequest objects to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call.
    ## Return:
    - list of IssuingEmbossingRequest objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=requests, user=user)

def query(
    limit=None, after=None, before=None, status=None, card_ids=None, 
    ids=None, tags=None, user=None
):
    """# Retrieve IssuingEmbossingRequests
    Receive a generator of IssuingEmbossingRequest objects previously created in the Stark Infra API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [list of strings, default None]: filter for status of retrieved objects. ex: ["active", "blocked", "canceled", "expired"]
    - card_ids [list of string, default null]: list of card_ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call.
    ## Return:
    - generator of IssuingEmbossingRequest objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        card_ids=card_ids,
        ids=ids,
        tags=tags,
        user=user,
    )


def page(
    cursor=None, limit=None, after=None, before=None, status=None, card_ids=None, 
    ids=None, tags=None, user=None
):
    """# Retrieve paged IssuingEmbossingRequests
    Receive a list of IssuingEmbossingRequest objects previously created in the Stark Infra API and the cursor to the next page.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. Max = 100. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [list of strings, default None]: filter for status of retrieved objects. ex: ["active", "blocked", "canceled", "expired"]
    - card_ids [list of string, default null]: list of card_ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call.
    ## Return:
    - list of IssuingEmbossingRequest objects with updated attributes
    - cursor to retrieve the next page of IssuingEmbossingRequest objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        card_ids=card_ids,
        ids=ids,
        tags=tags,
        user=user,
    )


def get(id, user=None):
    """# Retrieve a specific IssuingEmbossingRequests
    Receive a single IssuingEmbossingRequests object previously created in the Stark Infra API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call.
    ## Return:
    - IssuingEmbossingRequests object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)
