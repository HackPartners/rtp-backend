#Adding to pythonpath
from flask import Flask
from flask_restful import Api
from resources import DelayClaimResource

app = Flask(__name__)
api = Api(app)

# This function enables CORS in all requests
@app.after_request
def after_request(response):
  response.headers.add("Access-Control-Allow-Origin", "*")
  response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
  response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE")
  return response

api.add_resource(DelayClaimResource, "/delayClaim")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)

