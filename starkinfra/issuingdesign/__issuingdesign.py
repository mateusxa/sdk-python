from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_date, check_datetime
from ..utils import rest


class IssuingDesign(Resource):
    """# IssuingDesign object
    The IssuingDesign objects display information on the card and card package designs available to your Workspace.
    ## Attributes (return-only):
    - id [string]: unique id returned when IssuingDesign is created. ex: "5656565656565656"
    - name [long]: card or package name ex: 'stark-plastic-dark-001'
    - tags [list of strings, default null]: list of strings for tagging. ex: ["travel", "food"]
    - embosserIds [list of string]: list of embosser unique ids ex: ["5136459887542272", "5136459887542273"]
    - subIssuerId [string]: sub issuer unique id. ex: "5136459887542272"
    - updated [datetime.datetime]: latest update datetime for the IssuingDesign. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - created [datetime.datetime]: creation datetime for the IssuingDesign. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, 
        id=None, name=None, tags=None, embosserIds=None, subIssuerId=None, created=None, updated=None
    ):
        Resource.__init__(self, id=id)

        self.name = name
        self.tags = tags
        self.embosserIds = embosserIds
        self.subIssuerId = subIssuerId
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": IssuingDesign, "name": "IssuingDesign"}

def query(
    limit=None, after=None, before=None, tags=None, ids=None, 
    subIssuerIds=None, embosserIds=None, user=None
):
    """# Retrieve IssuingDesigns
    Receive a generator of IssuingDesign objects previously created in the Stark Infra API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - subIssuerIds [list of string, default null]: filter for subIssuerId of retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - embosserIds [list of string, default null]: filter for embosserId of retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call.
    ## Return:
    - generator of IssuingDesign objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        tags=tags,
        ids=ids,
        subIssuerIds=subIssuerIds,
        embosserIds=embosserIds,
        user=user,
    )


def page(
    cursor=None, limit=None, after=None, before=None, tags=None, ids=None, 
    subIssuerIds=None, embosserIds=None, user=None
):
    """# Retrieve paged IssuingDesigns
    Receive a list of IssuingDesign objects previously created in the Stark Infra API and the cursor to the next page.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. Max = 100. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - subIssuerIds [list of string, default null]: filter for subIssuerId of retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - embosserIds [list of string, default null]: filter for embosserId of retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call.
    ## Return:
    - list of IssuingDesign objects with updated attributes
    - cursor to retrieve the next page of IssuingDesign objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        tags=tags,
        ids=ids,
        subIssuerIds=subIssuerIds,
        embosserIds=embosserIds,
        user=user,
    )


def get(id, user=None):
    """# Retrieve a specific IssuingDesigns
    Receive a single IssuingDesigns object previously created in the Stark Infra API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call.
    ## Return:
    - IssuingDesigns object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)

def pdf(id, user=None):
    """# Retrieve a specific IssuingDesigns pdf file
    Receive a single IssuingDesigns pdf file generated in the Stark Bank API by its id.
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - IssuingDesigns pdf file
    """
    return rest.get_content(resource=_resource, id=id, user=user, sub_resource_name="pdf")
