from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime
from ..utils import rest


class IssuingHolder(Resource):
    """# IssuingHolder object
    The IssuingHolder describes a card holder that may group several cards.
    ## Parameters (required):
    - name [string]: card holder name.
    - tax_id [string]: card holder tax ID
    - external_id [string] card holder external ID
    ## Parameters (optional):
    - rules [list of IssuingRule, default []]: [EXPANDABLE] list of holder spending rules
    - tags [list of strings, default []]: list of strings for tagging. ex: ["travel", "food"]
    ## Attributes (return-only):
    - id [string]: unique id returned when IssuingHolder is created. ex: "5656565656565656"
    - status [string]: current IssuingHolder status. ex: "active", "blocked" or "canceled"
    - updated [datetime.datetime]: latest update datetime for the IssuingHolder. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - created [datetime.datetime]: creation datetime for the IssuingHolder. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, name, tax_id, external_id, id=None,  rules=None, status=None, tags=None, updated=None, created=None):
        Resource.__init__(self, id=id)
        self.name = name
        self.tax_id = tax_id
        self.external_id = external_id
        self.status = status
        self.rules = rules
        self.tags = tags
        self.updated = check_datetime(updated)
        self.created = check_datetime(created)


_resource = {"class": IssuingHolder, "name": "IssuingHolder"}


def create(holders, user=None):
    """# Create IssuingHolder
    Send a list of IssuingHolder objects for creation in the Stark Infra API
    ## Parameters (required):
    - holders [list of IssuingHolder objects]: list of IssuingHolder objects to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call
    ## Return:
    - list of IssuingHolder objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=holders, user=user)


def get(id, expand=None, user=None):
    """# Retrieve a specific IssuingHolder
    Receive a single IssuingHolder object previously created in the Stark Infra API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - expand [list of strings, default None]: fields to expand information. ex: ["rules"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call
    ## Return:
    - IssuingHolder object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, expand=expand, user=user)


def query(limit=None, after=None, before=None, status=None, tags=None, ids=None, expand=None, user=None):
    """# Retrieve IssuingHolders
    Receive a generator of IssuingHolder objects previously created in the Stark Infra API
    ## Parameters (optional):
    - limit [integer, default 100]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [string, default None]: filter for status of retrieved objects. ex: "paid" or "registered"
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - expand [list of strings, default None]: fields to expand information. ex: ["rules"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call
    ## Return:
    - generator of IssuingHolder objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_datetime(after),
        before=check_datetime(before),
        status=status,
        tags=tags,
        ids=ids,
        expand=expand,
        user=user,
    )


def page(limit=None, after=None, before=None, status=None, sort=None, tags=None, ids=None, expand=None, cursor=None, user=None):
    """# Retrieve IssuingHolders
    Receive a list of IssuingHolder objects previously created in the Stark Infra API and the cursor to the next page.
    ## Parameters (optional):
    - limit [integer, default 100]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [string, default None]: filter for status of retrieved objects. ex: "paid" or "registered"
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - expand [string, default None]: fields to expand information. ex: "rules, securityCode, number, expiration"
    - cursor [string, default None]: cursor returned on the previous page function call
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call
    ## Return:
    - list of IssuingHolder objects with updated attributes
    - cursor to retrieve the next page of IssuingHolder objects
    """
    return rest.get_page(
        resource=_resource,
        limit=limit,
        after=check_datetime(after),
        before=check_datetime(before),
        sort=sort,
        status=status,
        tags=tags,
        ids=ids,
        expand=expand,
        cursor=cursor,
        user=user,
    )


def update(id, status=None, name=None, rules=None, tags=None, user=None):
    """# Update IssuingHolder entity
    Update an IssuingHolder by passing id, if it hasn't been paid yet.
    ## Parameters (required):
    - id [string]: IssuingHolder id. ex: '5656565656565656'
    ## Parameters (optional):
    - status [string]: You may block the IssuingHolder by passing 'blocked' in the status
    - name [string]: card holder name.
    - tags [list of strings]: list of strings for tagging
    - rules [list of dictionaries, default None]: list of dictionaries with "amount": int, "currencyCode": string, "id": string, "interval": string, "name": string pairs
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call
    ## Return:
    - target IssuingHolder with updated attributes
    """
    payload = {
        "status": status,
        "name": name,
        "rules": rules,
        "tags": tags,
    }
    return rest.patch_id(resource=_resource, id=id, user=user, payload=payload)


def delete(id, user=None):
    """# Delete an IssuingHolder entity
    Delete an IssuingHolder entity previously created in the Stark Infra API
    ## Parameters (required):
    - id [string]: IssuingHolder unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call
    ## Return:
    - deleted IssuingHolder object
    """
    return rest.delete_id(resource=_resource, id=id, user=user)