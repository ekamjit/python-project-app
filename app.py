import json

from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api

import min_cost_problem


class VisionJSONEncoder(json.JSONEncoder):
    def default(self, o):
        return json.JSONEncoder.default(self, o)


# instantiating Flask application
class MyConfig(object):
    RESTFUL_JSON = {"cls": VisionJSONEncoder}


# instantiating Flask application
app = Flask(__name__)
app.config.from_object(MyConfig)
CORS(app)
api = Api(app)


class CostCalculationResource(Resource):
    def post(self):
        """
        Post Request to get the minimum cost of transit
        :return: cost if calculated successfully, else 500
        """
        packets = request.args.get('packets')

        if request.args.get('packets') is None:
            return {"error": "No information passed"}, 400

        packets_list = packets.split(',')
        return {"cost": min_cost_problem.find_min_cost(packets_list)}, 200


api.add_resource(CostCalculationResource, "/cost")

if __name__ == '__main__':
    app.run(host="localhost", debug=False, port=8001)
