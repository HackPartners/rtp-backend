from flask_restful import Resource, reqparse, marshal_with, fields, request

from models import Journey, DelayClaim

import json

class DelayClaimResource(Resource):

    def post(self):
        print("starting...")

        response = {}

        params = request.json
        print(params)

        return response

