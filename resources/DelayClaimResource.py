import datetime, json
from flask_restful import Resource, request
from playhouse.shortcuts import model_to_dict

from services import DelayClaimRequestService
from models import DelayClaim

def convert_dict_date_string(d):

    def default(o):
        if type(o) is datetime.date or type(o) is datetime.datetime:
            return o.isoformat()

    json_string = json.dumps(d, default=default)
    return json.loads(json_string)

class DelayClaimResource(Resource):

    def get(self):
        """
            Retreives DelayClaim instances from the database as JSON objects. If returns a specific result.
        """

        response = []

        delay_claims = DelayClaim.select()

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
        print(params)

        dcrs = DelayClaimRequestService()
        delay_claim = dcrs.save_claim_request(params)

        response["id"] = delay_claim.id

        return response

