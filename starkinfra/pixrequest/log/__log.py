from ...utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.api import from_api_json
from starkcore.utils.checks import check_datetime, check_date
from ..__pixrequest import _resource as _pixrequest_resource


class Log(Resource):
    """# PixRequest.Log object
    Every time a PixRequest entity is modified, a corresponding PixRequest.Log
    is generated for the entity. This log is never generated by the user.
    ## Attributes:
    - id [string]: unique id returned when the log is created. ex: "5656565656565656"
    - created [datetime.datetime]: creation datetime for the log. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - type [string]: type of the PixRequest event which triggered the log creation. ex: "registered" or "paid"
    - errors [list of strings]: list of errors linked to this PixRequest event
    - request [PixRequest]: PixRequest entity to which the log refers to.
    """
    def __init__(self, id, created, type, errors, request):
        Resource.__init__(self, id=id)

        self.created = check_datetime(created)
        self.type = type
        self.errors = errors
        self.request = from_api_json(_pixrequest_resource, request)


_resource = {"class": Log, "name": "PixRequestLog"}


def get(id, user=None):
    """# Retrieve a specific PixRequest.Log
    Receive a single PixRequest.Log object previously created by the Stark Infra API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call
    ## Return:
    - PixRequest.Log object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, types=None, request_ids=None, reconciliation_id=None, user=None):
    """# Retrieve PixRequest.Logs
    Receive a generator of PixRequest.Log objects previously created in the Stark Infra API
    ## Parameters (optional):
    - limit [integer, default 100]: maximum number of objects to be retrieved. Max = 100. ex: 35
    - after [datetime.date or string, default None]: date filter for objects created after a specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created before a specified date. ex: datetime.date(2020, 3, 10)
    - types [list of strings, default None]: filter retrieved objects by types. Options: "sent", "denied", "failed", "created", "success", "approved", "credited", "refunded", "processing".
    - request_ids [list of strings, default None]: list of PixRequest ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - reconciliation_id [string]: PixRequest reconciliation id to filter retrieved objects. ex: "b77f5236-7ab9-4487-9f95-66ee6eaf1781"
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call
    ## Return:
    - generator of PixRequest.Log objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        request_ids=request_ids,
        reconciliation_id=reconciliation_id,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, types=None, request_ids=None, reconciliation_id=None, user=None):
    """# Retrieve paged PixRequest.Logs
    Receive a list of up to 100 PixRequest.Log objects previously created in the Stark Infra API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. Max = 100. ex: 35
    - after [datetime.date or string, default None]: date filter for objects created after a specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created before a specified date. ex: datetime.date(2020, 3, 10)
    - types [list of strings, default None]: filter retrieved objects by types. Options: "sent", "denied", "failed", "created", "success", "approved", "credited", "refunded", "processing".
    - request_ids [list of strings, default None]: list of PixRequest IDs to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - reconciliation_id [string]: PixRequest reconciliation id to filter retrieved objects. ex: "b77f5236-7ab9-4487-9f95-66ee6eaf1781"
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call
    ## Return:
    - list of PixRequest.Log objects with updated attributes
    - cursor to retrieve the next page of PixRequest.Log objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        request_ids=request_ids,
        reconciliation_id=reconciliation_id,
        user=user,
    )