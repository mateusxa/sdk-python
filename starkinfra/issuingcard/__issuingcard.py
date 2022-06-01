from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_date, check_datetime
from ..utils import rest
from ..__issuingrule import parse_rules


class IssuingCard(Resource):

    """# IssuingCard object
    The IssuingCard object displays the information of the cards created in your Workspace.
    Sensitive information will only be returned when the "expand" parameter is used, to avoid security concerns.
    ## Parameters (required):
    - holder_name [string]: card holder name. ex: "Tony Stark"
    - holder_tax_id [string]: card holder tax ID. ex: "012.345.678-90"
    - holder_external_id [string]: card holder unique id, generated by the user to avoid duplicated holders. ex: "my-entity/123"
    ## Parameters (optional):
    - display_name [string, default None]: card displayed name. ex: "ANTHONY STARK"
    - rules [list of IssuingRule, default []]: [EXPANDABLE] list of card spending rules.
    - bin_id [string, default None]: BIN ID to which the card is bound. ex: "53810200"
    - tags [list of strings, default None]: list of strings for tagging. ex: ["travel", "food"]
    - street_line_1 [string, default sub-issuer street line 1]: card holder main address. ex: "Av. Paulista, 200"
    - street_line_2 [string, default sub-issuer street line 2]: card holder address complement. ex: "Apto. 123"
    - district [string, default sub-issuer district]: card holder address district / neighbourhood. ex: "Bela Vista"
    - city [string, default sub-issuer city]: card holder address city. ex: "Rio de Janeiro"
    - state_code [string, default sub-issuer state code]: card holder address state. ex: "GO"
    - zip_code [string, default sub-issuer zip code]: card holder address zip code. ex: "01311-200"
    ## Attributes (return-only):
    - id [string]: unique id returned when IssuingCard is created. ex: "5656565656565656"
    - holder_id [string]: card holder unique id. ex: "5656565656565656"
    - type [string]: card type. ex: "virtual"
    - status [string]: current IssuingCard status. ex: "active", "blocked", "canceled", "expired".
    - number [string]: [EXPANDABLE] masked card number. Expand to unmask the value. ex: "123".
    - security_code [string]: [EXPANDABLE] masked card verification value (cvv). Expand to unmask the value. ex: "123".
    - expiration [datetime.datetime]: [EXPANDABLE] masked card expiration datetime. Expand to unmask the value. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0).
    - updated [datetime.datetime]: latest update datetime for the IssuingCard. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - created [datetime.datetime]: creation datetime for the IssuingCard. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, holder_name, holder_tax_id, holder_external_id, display_name=None, rules=None, bin_id=None,
                 tags=None, street_line_1=None, street_line_2=None, district=None, city=None, state_code=None,
                 zip_code=None, id=None, holder_id=None, type=None, status=None, number=None, security_code=None,
                 expiration=None, created=None, updated=None):
        Resource.__init__(self, id=id)

        self.holder_name = holder_name
        self.holder_tax_id = holder_tax_id
        self.holder_external_id = holder_external_id
        self.display_name = display_name
        self.rules = parse_rules(rules)
        self.bin_id = bin_id
        self.tags = tags
        self.street_line_1 = street_line_1
        self.street_line_2 = street_line_2
        self.district = district
        self.city = city
        self.state_code = state_code
        self.zip_code = zip_code
        self.holder_id = holder_id
        self.type = type
        self.status = status
        self.number = number
        self.security_code = security_code
        self.expiration = check_datetime(expiration)
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": IssuingCard, "name": "IssuingCard"}


def create(cards, expand=None, user=None):
    """# Create IssuingCards
    Send a list of IssuingCard objects for creation at the Stark Infra API
    ## Parameters (required):
    - cards [list of IssuingCard objects]: list of IssuingCard objects to be created in the API
    ## Parameters (optional):
    - expand [list of strings, default []]: fields to expand information. ex: ["rules", "security_code", "number", "expiration"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call
    ## Return:
    - list of IssuingCard objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=cards, expand=expand, user=user)


def query(limit=None, ids=None, after=None, before=None, status=None, types=None, holder_ids=None, tags=None,
          expand=None, user=None):
    """# Retrieve IssuingCards
    Receive a generator of IssuingCards objects previously created in the Stark Infra API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [list of strings, default None]: filter for status of retrieved objects. ex: ["active", "blocked", "canceled", "expired"]
    - types [list of strings, default None]: card type. ex: ["virtual"]
    - holder_ids [list of strings]: card holder IDs. ex: ["5656565656565656", "4545454545454545"]
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - expand [list of strings, default []]: fields to expand information. ex: ["rules", "security_code", "number", "expiration"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call
    ## Return:
    - generator of IssuingCards objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        ids=ids,
        after=check_date(after),
        before=check_date(before),
        status=status,
        types=types,
        holder_ids=holder_ids,
        tags=tags,
        expand=expand,
        user=user,
    )


def page(cursor=None, limit=None, ids=None, after=None, before=None, status=None, types=None, holder_ids=None,
         tags=None, expand=None, user=None):
    """# Retrieve paged IssuingCards
    Receive a list of IssuingCards objects previously created in the Stark Infra API and the cursor to the next page.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [list of strings, default None]: filter for status of retrieved objects. ex: ["active", "blocked", "canceled", "expired"]
    - types [list of strings, default None]: card type. ex: ["virtual"]
    - holder_ids [list of strings]: card holder IDs. ex: ["5656565656565656", "4545454545454545"]
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - expand [list of strings, default []]: fields to expand information. ex: ["rules", "security_code", "number", "expiration"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call
    ## Return:
    - list of IssuingCards objects with updated attributes
    - cursor to retrieve the next page of IssuingCards objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        ids=ids,
        after=check_date(after),
        before=check_date(before),
        status=status,
        types=types,
        holder_ids=holder_ids,
        tags=tags,
        expand=expand,
        user=user,
    )


def get(id, expand=None, user=None):
    """# Retrieve a specific IssuingCards
    Receive a single IssuingCards object previously created in the Stark Infra API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - expand [list of strings, default None]: fields to expand information. ex: ["rules", "security_code", "number", "expiration"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call
    ## Return:
    - IssuingCards object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, expand=expand, user=user)


def update(id, status=None, display_name=None, rules=None, tags=None, user=None):
    """# Update IssuingCard entity
    Update an IssuingCard by passing id.
    ## Parameters (required):
    - id [string]: IssuingCard id. ex: '5656565656565656'
    ## Parameters (optional):
    - status [string, default None]: You may block the IssuingCard by passing 'blocked' or activate by passing 'active' in the status
    - display_name [string, default None]: card displayed name
    - rules [list of dictionaries, default None]: list of dictionaries with "amount": int, "currencyCode": string, "id": string, "interval": string, "name": string pairs.
    - tags [list of strings]: list of strings for tagging
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call
    ## Return:
    - target IssuingCard with updated attributes
    """
    payload = {
        "status": status,
        "display_name": display_name,
        "rules": rules,
        "tags": tags,
    }
    return rest.patch_id(resource=_resource, id=id, user=user, payload=payload)


def cancel(id, user=None):
    """# Cancel an IssuingCard entity
    Cancel an IssuingCard entity previously created in the Stark Infra API
    ## Parameters (required):
    - id [string]: IssuingCard unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call
    ## Return:
    - canceled IssuingCard object
    """
    return rest.delete_id(resource=_resource, id=id, user=user)
