import datetime, json
from flask_restful import Resource, request
from playhouse.shortcuts import model_to_dict
from decimal import Decimal
from enum import Enum

from services import DelayClaimRequestService
from models import DelayClaim, ClaimValidation, Journey

def convert_dict_date_string(d):

    def default(o):

        if type(o) is Decimal:
            return float(o)

        if type(o) is datetime.date or type(o) is datetime.datetime:
            return o.isoformat()

    json_string = json.dumps(d, default=default)
    return json.loads(json_string)

class DelayClaimResource(Resource):

    def get(self):
        """
            Retreives DelayClaim instances from the database as JSON objects. If returns a specific result.
        """

        args = request.args

        response = []

        clause = None

        
        if "id" in args:
            clause = DelayClaim.id == args["id"]

        if "identification" in args:
            clause = ClaimValidation.journey_identifier == args["identification"]

        delay_claims = (DelayClaim.select()
                            .join(ClaimValidation)
                            .where(clause))

        for delay_claim in delay_claims:
            d = model_to_dict(delay_claim, backrefs=True, recurse=True)

            d_json = convert_dict_date_string(d)
            response.append(d_json)

        return response

    def put(self):
        """
            Adds a DelayCalim instance to the databse, including its respective PaymentDetails, ContactDetails, Journey, and ClaimValidation objects.
        """

        response = {}

        params = request.json

        dcrs = DelayClaimRequestService()
        delay_claim = dcrs.save_claim_request(params)

        response["id"] = delay_claim.id

        return response

    def post(self):

        response = {}

        params = request.json

        claim_id = None

        if not "claimId" in params or not params["claimId"]: 
            return {
                "status": "ERROR",
                "message": "claimId parameter is required"
            }

        print(params)

        c_arr = (DelayClaim
                    .select()
                    .join(ClaimValidation)
                    .join(Journey, on=DelayClaim.journey==Journey.id)
                    .where(ClaimValidation.journey_identifier == claim_id))

        print(c_arr)

        if c_arr.count() == 0:
            return {
                "status": "DOES_NOT_EXIST",
                "message": "claim does not exist"
            }

        c = c_arr[0]

        v = c.claim_validation
        j = c.journey

        if "identification" in params and params["identification"]:
            v.journey_identifier = params["identification"]

        if "ticketClass" in params and params["ticketClass"]:
            j.ticket_class = params["ticketClass"]

        if "ticketType" in params and params["ticketType"]:
            j.ticket_class = params["ticketType"]

        if "fromDate" in params and params["fromDate"]:
            j.from_date = params["fromDate"]

        if "toDate" in params and params["toDate"]:
            j.to_date = params["toDate"]

        if "cost" in params and params["cost"]:
            j.cost = params["cost"]
            print(j.cost)

        j.save()
        v.save()
        c.save()

        return {
                "status": "SUCCESS",
                "message": "Successfully updated",
            }









