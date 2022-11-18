from starkcore.utils.api import from_api_json
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime, check_date
from ...utils import rest
from ..__issuingembossingrequest import _resource as _issuing_embossingrequest_resource


class Log(Resource):
    """# issuingembossingrequest.Log object
    Every time an IssuingEmbossingRequest entity is updated, a corresponding issuingembossingrequest.Log
    is generated for the entity. This log is never generated by the
    user, but it can be retrieved to check additional information
    on the IssuingEmbossingRequest.
    ## Attributes:
    - id [string]: unique id returned when the log is created. ex: "5656565656565656"
    - embossingrequest [IssuingEmbossingRequest]: IssuingEmbossingRequest entity to which the log refers to.
    - type [string]: type of the IssuingEmbossingRequest event which triggered the log creation. ex: "blocked", "canceled", "created", "unblocked", "updated"
    - created [datetime.datetime]: creation datetime for the log. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, id, embossingrequest, type, created):
        Resource.__init__(self, id=id)

        self.embossingrequest = from_api_json(_issuing_embossingrequest_resource, embossingrequest)
        self.type = type
        self.created = check_datetime(created)


_resource = {"class": Log, "name": "IssuingEmbossingRequestLog"}


def get(id, user=None):
    """# Retrieve a specific issuingembossingrequest.Log
    Receive a single issuingembossingrequest.Log object previously created by the Stark Infra API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call.
    ## Return:
    - issuingembossingrequest.Log object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(ids=None, limit=None, after=None, before=None, types=None, embossingrequest_ids=None, user=None):
    """# Retrieve issuingembossingrequest.Log
    Receive a generator of issuingembossingrequest.Log objects previously created in the Stark Infra API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - types [list of strings, default None]: filter for log event types. ex: ["created", "blocked"]
    - embossingrequest_ids [list of strings, default None]: list of IssuingEmbossingRequest ids to filter logs. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call.
    ## Return:
    - generator of issuingembossingrequest.Log objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        ids=ids,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        embossingrequest_ids=embossingrequest_ids,
        user=user,
    )


def page(cursor=None, ids=None, limit=None, after=None, before=None, types=None, embossingrequest_ids=None, user=None):
    """# Retrieve paged issuingembossingrequest.Log
    Receive a list of up to 100 issuingembossingrequest.Log objects previously created in the Stark Infra API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - types [list of strings, default None]: filter for log event types. ex: ["created", "blocked"]
    - embossingrequest_ids [list of strings, default None]: list of IssuingEmbossingRequest ids to filter logs. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call.
    ## Return:
    - list of issuingembossingrequest.Log objects with updated attributes
    - cursor to retrieve the next page of issuingembossingrequest.Log objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        ids=ids,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        embossingrequest_ids=embossingrequest_ids,
        user=user,
    )