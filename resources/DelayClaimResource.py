from flask_restful import Resource, reqparse, marshal_with, fields

from models import Journey, DelayClaim

payment_fields = {
    'paymentType': fields.String,
    'accountNumber': fields.String,
    'sortcode': fields.String
}

contact_details = {
    'title': fields.String,
    'firstName': fields.String,
    'lastName': fields.String,
    'address': fields.String,
    'email': fields.String,
    'postcode': fields.String
}

delay_claim = {
    'fromStation': fields.String,
    'toStation': fields.String,
    'ticketClass': fields.String,
    'ticketType': fields.String,
    'fromDate': fields.DateTime,
    'toDate': fields.DateTime,
    'journeyDate': fields.DateTime,
    'cost': fields.Float
}

user_fields = {
    'image64': fields.String,
    'delayClaim': fields.Nested(delay_claim),
    'contactDetails': fields.Nested(contact_details),
    'payment': fields.Nested(payment_fields),
}

class DelayClaimResource(Resource):

    def post(self):
        print("starting...")

        response = {}

        return response

