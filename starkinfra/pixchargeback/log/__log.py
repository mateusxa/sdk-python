from starkcore.utils.checks import check_datetime, check_date
from ..__pixchargeback import _resource as _pixchargeback_resource
from starkcore.utils.resource import Resource
from starkcore.utils.api import from_api_json
from ...utils import rest


class Log(Resource):
    """# pixchargeback.Log object
    Every time a PixChargeback entity is modified, a corresponding PixChargeback.Log
    is generated for the entity. This log is never generated by the user.
    ## Attributes:
    - id [string]: unique id returned when the log is created. ex: "5656565656565656"
    - chargeback [PixChargeback]: PixChargeback entity to which the log refers to.
    - type [string]: type of the PixChargeback event which triggered the log creation. ex: "created", "failed", "delivering", "delivered", "closed", "canceled"
    - errors [list of strings]: list of errors linked to this PixChargeback event
    - created [datetime.datetime]: creation datetime for the log. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """
    def __init__(self, id, chargeback, type, errors, created):
        Resource.__init__(self, id=id)

        self.chargeback = from_api_json(_pixchargeback_resource, chargeback)
        self.type = type
        self.errors = errors
        self.created = check_datetime(created)


_resource = {"class": Log, "name": "PixChargebackLog"}


def get(id, user=None):
    """# Retrieve a specific PixChargeback.Log
    Receive a single PixChargeback.Log object previously created by the Stark Infra API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call.
    ## Return:
    - PixChargeback.Log object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(ids=None, limit=None, after=None, before=None, types=None, chargeback_ids=None, user=None):
    """# Retrieve PixChargeback.Logs
    Receive a generator of PixChargeback.Log objects previously created in the Stark Infra API
    ## Parameters (optional):
    - ids [list of strings, default None]: Log ids to filter PixChargeback Logs. ex: ["5656565656565656"]
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None]: date filter for objects created after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created before a specified date. ex: datetime.date(2020, 3, 10)
    - types [list of strings, default None]: filter retrieved objects by types. ex: ["created", "failed", "delivering", "delivered", "closed", "canceled"]
    - chargeback_ids [list of strings, default None]: list of PixChargeback IDs to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call.
    ## Return:
    - generator of PixChargeback.Log objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        ids=ids,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        chargeback_ids=chargeback_ids,
        user=user,
    )


def page(cursor=None, ids=None, limit=None, after=None, before=None, types=None, chargeback_ids=None, user=None):
    """# Retrieve paged PixChargeback.Logs
    Receive a list of up to 100 PixChargeback.Log objects previously created in the Stark Infra API and the cursor to the next page.
    Use this function instead of query if you want to manually page your chargebacks.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - ids [list of strings, default None]: Log ids to filter PixChargeback Logs. ex: ["5656565656565656"]
    - limit [integer, default 100]: maximum number of objects to be retrieved. Max = 100. ex: 35
    - after [datetime.date or string, default None]: date filter for objects created after a specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created before a specified date. ex: datetime.date(2020, 3, 10)
    - types [list of strings, default None]: filter retrieved objects by types. ex: ["created", "failed", "delivering", "delivered", "closed", "canceled"]
    - chargeback_ids [list of strings, default None]: list of PixChargeback IDs to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call.
    ## Return:
    - list of PixChargeback.Log objects with updated attributes
    - cursor to retrieve the next page of PixChargeback.Log objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        ids=ids,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        chargeback_ids=chargeback_ids,
        user=user,
    )
